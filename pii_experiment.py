# pii_experiment.py

import os
import time
from extract import extract_with_pypdf2
import engine_ner
import engine_llm_pii

def run_pii_lab(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "cv_file", file_name)
    text = extract_with_pypdf2(path)

    # List methods
    methods = [
        ("GLiNER", lambda t: engine_ner.clean_with_gliner(t)),
        ("LLM-Llama3.2", lambda t: engine_llm_pii.clean_with_llm(t, "llama3.2")),
        ("LLM-Mistral", lambda t: engine_llm_pii.clean_with_llm(t, "mistral"))
    ]

    print(f"--- TESTE BEGINNING TO: {file_name} ---")

    for name, func in methods:
        start = time.time()
        
        # Executa a função do método
        result = func(text)
        
        duration = time.time() - start
        
        print(f"\n[{name}]")
        print(f"Processing time: {duration:.2f}s")
        print(f"Preview: {result[:200]}...") # It only shows the beginning.
        #print(f"Preview: {result}")
        print("-" * 30)

if __name__ == "__main__":
    #run_pii_lab("ByungjinPark.pdf")
    run_pii_lab("John_Doe_ModerncvTheme_CV.pdf")