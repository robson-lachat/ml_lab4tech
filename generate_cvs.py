# generate_cvs.py

import os
from datetime import datetime
from extract import extract_with_pypdf2
from llm_annote import annote

def generate_fake_cv(job_text, match_type, provider):
    
    prompt = f"""
    Based on the following JOB DESCRIPTION, generate a realistic fake CV in HTML format.
    The candidate should be a {match_type} for this position.
    
    MATCH TYPES:
    - 'High Match': Candidate meets all requirements and has extra experience.
    - 'Partial Match': Candidate has some skills but lacks key experience or technologies.
    - 'No Match': Candidate is from a completely different field.

    Return ONLY the HTML code (start with <html> and end with </html>).
    Use CSS inside a <style> tag to make it look like a professional resume.

    JOB DESCRIPTION:
    {job_text}
    """
    
    # Use function annote end send job text + prompt + llm
    return annote(job_text, prompt, provider=provider)

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Config file and target role
    provider_name = "mistral" # Ex: "mistal", "openai" ...
    target_role = "FullStack_Python_Django" # Role EPFL

    # 1. Extract job text (put PDF in folder /job_descriptions)
    job_pdf_name = "Spécialiste systèmes & développement Full-Stack (Python_Django) - Offre d'emploi chez EPFL - jobup.ch.pdf"
    job_pdf = os.path.join(base_path, "job_descriptions", job_pdf_name)
    job_text = extract_with_pypdf2(job_pdf)

    # 2. Type CVs generate (Exercice 2)
    types_to_generate = [
        ("high_match", "High Match"),
        ("high_match", "High Match"),
        ("partial_match", "Partial Match"),
        ("partial_match", "Partial Match"),
        ("no_match", "No Match"),
        ("no_match", "No Match"),
        ("no_match", "No Match")
    ]

    print(f"Satrting a new generation with {provider_name.upper()}...")

    for i, (m_label, m_type) in enumerate(types_to_generate, 1):
        # Generate timestamp in the requested format: 20260417_134620
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Assemble filename
        filename = f"{provider_name}_{target_role}_{m_label}_{i}_{timestamp}.html"

        print(f"\n[{i}/7] Generating: {filename}...")

        html_content = generate_fake_cv(job_text, m_type, provider_name)
        
        # Cleaning html file
        if "<html>" in html_content:
            html_content = html_content[html_content.find("<html>") : html_content.find("</html>") + 7]
        
        # Save .html in folder cv_file
        save_path = os.path.join(base_path, "cv_file", filename)

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Done! Saved at: {save_path}")