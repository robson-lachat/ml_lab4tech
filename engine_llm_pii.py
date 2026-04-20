# engine_llm_pii.py

from llm_annote import annote

def clean_with_llm(text, model_name="mistral"):
    instruction = "Replace names, emails and phones with [REDACTED]. Return ONLY the text." 
    
    # Reuse llm_annote.py
    return annote(text, instruction, provider="ollama", model=model_name)