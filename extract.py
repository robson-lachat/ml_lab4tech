from PyPDF2 import PdfReader

def extract_with_pypdf2(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # evita None
                text += page_text + "\n"

        return text

    except Exception as e:
        print(f"Error read PDF: {e}")
        return ""
    
if __name__ == "__main__":
    content = extract_with_pypdf2("cv.pdf")
    print(content)
