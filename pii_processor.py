# pii_processor.py

import os
from extract import extract_with_pypdf2
from llm_annote import annote

def processs_with_llm(file_path: str, prompt_instruction: str) -> str:
    # Extract text of function file extrac.py
    text = extract_with_pypdf2(file_path)

    # Send for Mistral llm_annote.py
    annoted_text = annote(text, prompt_instruction)

    return annoted_text

if __name__ == "__main__":
    # Create path for PDF files
    # Get directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Get folders and files
    folder_path = os.path.join(base_path, "cv_file")


    prompt_tests = [
        "Analyze this CV for a Web Developer position."
        "Analyze this CV for a DevOps position and tell us if they have the right tools.",
        "Summarize this CV in just 3 lines for a rushed recruiter.",
        "Analyze this CV and list main skills and experience level.",
        "Is this candidate suitable for a Senior DevOps role? Why?"
        #,"Hide personal information (email, name, address) by replacing it with [REDACTED]"
        #,"""Analyze this CV and answer:
        #    1. What are the main skills?
        #    2. What is the experience level?
        #    3. What are strengths and weaknesses?
        #    """
    ]

    # Loop for read all files PDF
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(f"\n{'='*60}")
            print(f"PROCESSING FILE: {filename}")
            print(f"{'='*60}")

    # Loop para testar cada prompt neste arquivo
            for p in prompt_tests:
                print(f"\n--- Test prompt: {p} ---")
                results = processs_with_llm(full_file_path, p)
                print(results)
    else:
        print(f"Erro: Pasta {folder_path} não encontrada.")