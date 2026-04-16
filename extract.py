# extract.py

import os
from PyPDF2 import PdfReader

def extract_with_pypdf2(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        print(f"Error read PDF at {file_path}: {e}")
        return ""
    
if __name__ == "__main__":
    # Get directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Get folders and files
    file_path = os.path.join(base_path, "cv_file", "Alexandre Silva.pdf")

    content = extract_with_pypdf2(file_path)
    print(content)