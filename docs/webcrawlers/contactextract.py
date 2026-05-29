import os
import re
import sys
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib3

# Suppress messy InsecureRequestWarning warnings in terminal screen
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Robust patterns for global email and phone discovery
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_PATTERN = re.compile(r"(?:\+94|0)[1-9][0-9]\s?[- ]?[0-9]{3}\s?[- ]?[0-9]{4}")

# Loose Title matching pattern to clean titles out of names if they bleed in
DESIGNATION_CLEAN_PATTERN = re.compile(
    r"\b(Senior Professor|Senior Lecturer|Assistant Lecturer|Professor|Lecturer|Instructor|Head|Dean|HOD|Probationary|Grade I|Grade II|II|I|Visiting|Chair)\b",
    re.IGNORECASE
)

# Skips pages that do not host individual personnel profiles
BLACKLIST_KEYWORDS = [
    'accreditation', 'scholarship', 'schedule', 'guidelines', 'structure', 'research', 'mile-stone', 'grants', 
    'partners-in-leaning','student-handbook', 'news', 'programme', 'internship', 'dissertation', 'exemption', 
    'calendar-of-dates', 'heads-of-the-department','library','student-resources','msu', 'curriculum', 'syllabus', 
    'fee', 'exam', 'admission', 'course','activity','ethics-review-committee','iqac','alumni','video-resources',
    'history', 'gallery', 'event', 'notice', 'download', 'publication'
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

# Persistent network session to speed up sequential loop downloads
session = requests.Session()
session.headers.update(HEADERS)
session.verify = False  # Global bypass for local university SSL configuration errors

def clean_extracted_name(name_str):
    """Removes any academic designation keywords that leaked into the name string."""
    if not name_str:
        return "Name Check Required"
    name_str = DESIGNATION_CLEAN_PATTERN.sub("", name_str)
    name_str = re.sub(r'^\s*[-–—,•|:]\s*|\s*[-–—,•|:]\s*\$', '', name_str)
    return " ".join(name_str.split()).strip()

def discover_name_on_profile(soup):
    """Finds the person's name on their profile page by checking top-level headings or title."""
    for tag_name in ['h1', 'h2', 'h3']:
        for heading in soup.find_all(tag_name):
            text = heading.get_text().strip()
            if any(title in text.lower() for title in ['prof', 'dr.', 'mr.', 'ms.', 'mrs.']):
                return clean_extracted_name(text)
                
    if soup.title and soup.title.string:
        try:
            # Iteratively processes delimiters to split safely
            title_text = soup.title.string
            for delimiter in ['|', '-']:
                if delimiter in title_text:
                    # Extracts the first contextual block before the divider safely
                    title_text = title_text.split(delimiter)[0]
            title_text = title_text.strip()
            
            if any(title in title_text.lower() for title in ['prof', 'dr.', 'mr.', 'ms.', 'mrs.', 'staff']):
                return clean_extracted_name(title_text.replace('Staff', '').replace('Profile', ''))
        except Exception:
            pass
            
    return "Name Check Required"

def discover_designation_on_profile(soup):
    """Scans the profile text elements to classify their exact academic rank."""
    page_text = soup.get_text(separator=" ")
    
    leader_match = re.search(r'\b(Head of Department|Head|HOD|Dean)\b', page_text, re.IGNORECASE)
    if leader_match:
        val = leader_match.group(0).lower()
        return "HOD" if val == 'hod' else leader_match.group(0).title()
        
    rank_match = re.search(r'\b(Senior Professor|Senior Lecturer|Assistant Lecturer|Lecturer|Professor)\s*(?:Grade\s*[IVX12i]+|[IVX12i]+|（Confirmed）|（Probationary）)?\b', page_text, re.IGNORECASE)
    if rank_match:
        return " ".join(rank_match.group(0).split()).title()
        
    return "Academic Staff"

def parse_details_from_snippet(text):
    """Uses contextual regex patterns to filter designations, phone lines, and formal names."""
    clean_text = " ".join(text.split())

    desig_match = DESIGNATION_CLEAN_PATTERN.search(clean_text)
    designation = desig_match.group(0).strip() if desig_match else "Lecturer / Academic Staff"
    
    leader_match = re.search(r'\b(Head of Department|Head|HOD|Dean)\b', clean_text, re.IGNORECASE)
    if leader_match:
        val = leader_match.group(0).lower()
        designation = "HOD" if val == 'hod' else leader_match.group(0).title()
    else:
        grade_match = re.search(r'\b(Senior Lecturer|Lecturer|Assistant Lecturer)\s*(?:Grade\s*[IVX12i]+|[IVX12i]+)?\b', clean_text, re.IGNORECASE)
        if grade_match:
            designation = " ".join(grade_match.group(0).split()).title()

    name_match = re.search(r"\b(?:Prof\.|Dr\.|Mr\.|Mrs\.|Ms\.|Ven\.)\s+(?:(?:[A-Z]\.\s*)+[A-Z][a-z]+|(?:[A-Z][a-z]+\s+)+[A-Z][a-z]+|[A-Z][a-z]+)", clean_text, re.IGNORECASE)
    raw_extracted_name = name_match.group(0).strip() if name_match else "Name Check Required"
    final_clean_name = clean_extracted_name(raw_extracted_name)

    phone_match = PHONE_PATTERN.search(clean_text)
    phone = phone_match.group(0) if phone_match else "N/A"

    return final_clean_name, designation, phone

def get_profile_links_from_directory(directory_url):
    """Scans the directory layout page to identify deep individual profile links universally."""
    profile_links = set()
    try:
        response = session.get(directory_url, timeout=15)
        if response.status_code != 200:
            print(f"[-] Directory connection rejected. Status Code: {response.status_code}")
            return []
        soup = BeautifulSoup(response.text, "html.parser")
        
        parsed_directory = urllib.parse.urlparse(directory_url)
        dir_parts = parsed_directory.netloc.replace("www.", "").split(".")
        uni_root_boundary = ".".join(dir_parts[-3:]) if "ac.lk" in directory_url else ".".join(dir_parts[-2:])
        
        for anchor in soup.find_all("a", href=True):
            href = anchor["href"].strip()
            if not href or href in ["#", "/", "index.php", "index.html", "home"]:
                continue
                
            full_url = urllib.parse.urljoin(directory_url, href)
            url_lower = full_url.lower()
            parsed_sublink = urllib.parse.urlparse(full_url)
            sublink_path = parsed_sublink.path.rstrip("/")
            
            if uni_root_boundary in parsed_sublink.netloc:
                if not sublink_path or sublink_path in ["", "/index.php"]:
                    continue
                if full_url != directory_url and full_url.rstrip('/') != directory_url.rstrip('/'):
                    if any(kw in url_lower for kw in BLACKLIST_KEYWORDS):
                        continue
                    if not any(x in url_lower for x in ['.pdf', '.jpg', '.png', '.zip', 'contact', 'about', 'lms']):
                        profile_links.add(full_url)
    except Exception as e:
        print(f"[-] Error collecting profile links: {e}")
    return list(profile_links)

def extract_contacts_deep(url):
    """Tries surface extraction first. If no multiple layout details are found, crawls the profile system."""
    records = []
    try:
        response = session.get(url, timeout=12)
        if response.status_code != 200:
            print(f"[-] Profile link rejected by server. Status Code: {response.status_code}")
            return records
        soup = BeautifulSoup(response.text, "html.parser")
        raw_text = soup.get_text(separator=" ")
    except Exception as e:
        print(f"[-] Connection failed to {url}: {e}")
        return records

    surface_emails = list(set(EMAIL_PATTERN.findall(raw_text)))
    
    # CASE 1: The page is a shared dynamic master table containing everyone's details
    if len(surface_emails) > 3:
        print(f"[+] Multiple emails found directly on landing directory page: {url}")
        for email in surface_emails:
            email_pos = raw_text.find(email)
            snippet = " ".join(raw_text[max(0, email_pos - 250):min(len(raw_text), email_pos + 250)].split())
            name, designation, phone = parse_details_from_snippet(snippet)
            records.append({
                "Name": name,
                "Email": email,
                "Designation": designation,
                "Phone": phone,
                "Profile URL": url
            })
            
    # CASE 2: The page is an individual personal profile biography path
    else:
        name = discover_name_on_profile(soup)
        designation = discover_designation_on_profile(soup)
        email = surface_emails[0] if surface_emails else "N/A"
        phone_match = PHONE_PATTERN.search(raw_text)
        phone = phone_match.group(0) if phone_match else "N/A"
        
        email = surface_emails[0] if surface_emails else "N/A"

        if name != "Name Check Required" or email != "N/A":
            # Mapped explicitly to avoid structural data shifting
            records.append({
                "Name": name,
                "Email": email,
                "Designation": designation,
                "Phone": phone,
                "Profile URL": url
            })
            
    return records


# --- RUNTIME EXECUTION CONTROLLER ---
if __name__ == "__main__":
    # Check if a URL was passed directly in the terminal invocation
    if len(sys.argv) > 1:
        TARGET_DIRECTORY = sys.argv[1].strip()
    else:
        print("💡 Tip: Next time, pass the URL straight into the command: python file.py <URL>")
        TARGET_DIRECTORY = input("Please paste the TARGET_DIRECTORY URL and press Enter: ").strip()

    # Absolute verification pattern checks
    if not TARGET_DIRECTORY.startswith(("http://", "https://")):
        print("[-] Error: Invalid URL layout. Please verify it starts with http:// or https://")
        sys.exit(1)
    
    print(f"\n[*] Commencing discovery pipeline on: {TARGET_DIRECTORY}")
    profile_urls = get_profile_links_from_directory(TARGET_DIRECTORY)
    print(f"[+] Identified {len(profile_urls)} potential faculty profile paths.")
    
    all_extracted_faculty = []

    # Process isolated routes sequentially

    for i, profile_url in enumerate(profile_urls, start=1):
        print(f"[{i}/{len(profile_urls)}] Processing: {profile_url}")
        results = extract_contacts_deep(profile_url)
        
        if results:
            all_extracted_faculty.extend(results)

        # Export structural details safely
        if all_extracted_faculty:
            df = pd.DataFrame(all_extracted_faculty)
            # Drop duplicates across clean matrix overlaps
            df.drop_duplicates(subset=['Email', 'Name'], keep='first', inplace=True)    

            # --- THE EXACT LOCATION WHERE COLUMN ORDER IS CHANGED ---
            # Re-indexing the layout list shifts columns instantly
            desired_order = ["Name", "Email", "Designation", "Phone", "Profile URL"]
            df = df[desired_order]
            # ---------------------------------------------------------

            # Clean naming module isolates domain strings
            domain = urllib.parse.urlparse(TARGET_DIRECTORY).netloc.replace("www.", "")
            output_file = f"extracted_faculty_{domain}.csv"
            df.to_csv(output_file, index=False)
            print(f"\n[Done] Pipeline saved {len(df)} records safely inside '{output_file}'!")
        else:
            print("\n[-] Pipeline closed. No contact cards could be mapped successfully.")