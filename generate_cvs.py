# generate_cvs.py

import os
import time
from datetime import datetime
from extract import extract_with_pypdf2
from llm_annote import annote

def generate_fake_cv(job_text, match_type, provider, model_name=None):
    
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
    
    # Use function annote end send job text + prompt + llm + model
    return annote(job_text, prompt, provider=provider, model=model_name)

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Config provider and models
    provider_name = "ollama" # Ex: "mistal", "openai", "ollama" ...
    local_models = ["llama3.2", "mistral", "phi3"]

    # Role EPFL
    target_role = "FullStack_Python_Django"

    # 1. Extract job text (put PDF in folder /job_descriptions)
    job_pdf_name = "Spécialiste systèmes & développement Full-Stack (Python_Django) - Offre d'emploi chez EPFL - jobup.ch.pdf"
    job_pdf = os.path.join(base_path, "job_descriptions", job_pdf_name)
    job_text = extract_with_pypdf2(job_pdf)

    # 2. Type CVs generate (Exercice 2)
    types_to_generate = [
        ("high_match", "High Match"),
        #("high_match", "High Match"),
        ("partial_match", "Partial Match"),
        #("partial_match", "Partial Match"),
        #("no_match", "No Match"),
        #("no_match", "No Match"),
        ("no_match", "No Match")
    ]

    print(f"Satrting a new generation with {provider_name.upper()}...")

  
    for model in local_models:
            print(f"\n>>> TESTING MODEL: {model.upper()} <<<")

            for i, (m_label, m_type) in enumerate(types_to_generate, 1):

                # MARKS THE BEGINNING
                start_process = time.time()

                # Generate timestamp in the requested format: 20260417_134620
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                # Assemble filename
                filename = f"{provider_name}_{model}_{target_role}_{m_label}_{i}_{timestamp}.html"

                print(f"\n[{i}/{len(types_to_generate)}] Generating: {filename}...")

                html_content = generate_fake_cv(job_text, m_type, provider_name, model_name=model)
                
                # Cleaning html file
                if "<html>" in html_content:
                    html_content = html_content[html_content.find("<html>") : html_content.find("</html>") + 7]
                
                # Save .html in folder cv_file
                save_path = os.path.join(base_path, "cv_file", filename)

                # MARK THE END AND CALCULATE
                end_process = time.time()
                duration = end_process - start_process
                finish_time = datetime.now().strftime("%H:%M:%S")

                # LOG PERFOMANCE
                

                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(html_content)

                print(f"Done! Saved at: {save_path}")