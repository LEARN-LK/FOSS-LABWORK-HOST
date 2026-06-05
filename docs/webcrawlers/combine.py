import os
import re

# Ask the user for the folder containing the text files
folder_path = input("Enter the path to the folder with your text files: ")

if not os.path.isdir(folder_path):
    print(f"Error: The folder '{folder_path}' does not exist.")
else:
    # Ask for the output filename
    output_filename = input(
        "Enter the name for the combined output file (e.g., all_emails.txt): "
    )

    # Use a set instead of a list to automatically remove duplicate emails
    unique_emails = set()

    # Regex pattern to find standard email formats
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Loop through every file in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Only process files ending in .txt
            if file.endswith(".txt") and file != output_filename:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                        # Find all emails in the current file
                        found_emails = re.findall(email_pattern, text)
                        # Strip spaces and add to our unique collection
                        for email in found_emails:
                            unique_emails.add(email.strip())
                except Exception as e:
                    print(f"Could not read file {file}: {e}")

    # Write all combined, clean emails to the final file
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for email in sorted(unique_emails):
            output_file.write(email + "\n")

    print(
        f"\nSuccess! Combined {len(unique_emails)} unique emails into '{output_filename}'."
    )
