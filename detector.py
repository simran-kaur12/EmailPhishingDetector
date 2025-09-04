import os
from utils.email_parser import parse_email

# Phishing keywords
PHISHING_KEYWORDS = [
    "verify your account",
    "urgent",
    "password reset",
    "bank",
    "click here",
    "login",
    "suspend",
    "account locked"
]

def check_phishing(email_text):
    email_text_lower = email_text.lower()
    score = sum([1 for word in PHISHING_KEYWORDS if word in email_text_lower])
    
    if score >= 2:
        return "⚠️ Potential Phishing Email"
    elif score == 1:
        return "⚠️ Suspicious Email"
    else:
        return "✅ Likely Safe Email"

if __name__ == "__main__":
    # Path to emails folder
    emails_folder = os.path.join(os.path.dirname(__file__), "emails")
    
    # Get all .eml files in folder
    email_files = [f for f in os.listdir(emails_folder) if f.endswith(".eml")]
    
    if not email_files:
        print("No .eml files found in the emails/ folder.")
    
    for file_name in email_files:
        file_path = os.path.join(emails_folder, file_name)
        email_content = parse_email(file_path)
        result = check_phishing(email_content)
        print(f"{file_name}: {result}")
