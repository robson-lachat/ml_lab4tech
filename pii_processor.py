from extract import extract_with_pypdf2
from llm_annote import annote

def processs_with_llm(file_path: str) -> str:
    text = extract_with_pypdf2(file_path)
    annoted_text = annote(text)
    return annoted_text