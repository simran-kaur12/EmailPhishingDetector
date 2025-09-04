# Simple helper to parse .eml files or email text
def parse_email(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
