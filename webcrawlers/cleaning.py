import os
import re

# Prompt the user for the input filename
input_filename = input("Enter the name of the input text file (e.g., emails.txt): ")

# Check if the file actually exists before proceeding
if not os.path.exists(input_filename):
    print(f"Error: The file '{input_filename}' was not found.")
else:
    # Prompt for the output filename
    output_filename = input(
        "Enter the name for the cleaned output file (e.g., cleaned.txt): "
    )

    # Read the original file contents
    with open(input_filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Use regex to find all email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)

    # Clean whitespace from the extracted emails
    cleaned_emails = [email.strip() for email in emails if email.strip()]

    # Write the cleaned emails to the user-specified output file
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for email in cleaned_emails:
            output_file.write(email + "\n")

    print(
        f"Success! Found {len(cleaned_emails)} emails and saved them to '{output_filename}'."
    )
