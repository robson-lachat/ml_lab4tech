# generate_cvs.py

import os
from extract import extract_with_pypdf2
from llm_annote import annote

def generate_fake_cv(job_text, match_type):
    # Specific instructions for Mistral to generate the CV
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
    
    # Use function annote end send job text to + prompt
    return annote(job_text, prompt)

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Extract job text (put PDF in folder job_descriptions)
    job_pdf = os.path.join(base_path, "job_descriptions", "Spécialiste systèmes & développement Full-Stack (Python_Django) - Offre d'emploi chez EPFL - jobup.ch.pdf")
    job_text = extract_with_pypdf2(job_pdf)

    # 2. Type CVs generate (Exercice 2)
    types_to_generate = [
        ("high_1", "High Match"),
        ("high_2", "High Match"),
        ("partial_1", "Partial Match"),
        ("partial_2", "Partial Match"),
        ("no_match_1", "No Match"),
        ("no_match_2", "No Match"),
        ("no_match_3", "No Match")
    ]

    for filename, m_type in types_to_generate:
        print(f"Generate CV: {filename} ({m_type})...")
        html_content = generate_fake_cv(job_text, m_type)
        
        # Clining html file
        if "<html>" in html_content:
            html_content = html_content[html_content.find("<html>") : html_content.find("</html>") + 7]
        
        # Save .html in folder cv_file
        save_path = os.path.join(base_path, "cv_file", f"{filename}.html")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Save in: {save_path}")