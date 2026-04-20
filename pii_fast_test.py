# pii_fast_test.py
import time
import engine_ner
import engine_llm_pii

# 1. TEXTO DE SIMULAÇÃO (Curto e com dados sensíveis)
SAMPLE_TEXT = """
CANDIDATE PROFILE:
Name: Alexandre Silva Rodrigues Lachat
Email: alex.lachat.2026@gmail.com
Address: Av. das Forças Armadas, 123, Lisboa, Portugal.
Phone: +351 912 345 678
Date of Birth: 15/05/1985
Goal: Senior Web Developer position with 10 years of experience in Python and Django.
"""

def run_fast_experiment():
    # Lista de métodos (A mesma que você já preparou)
    methods = [
        ("GLiNER (NER)", lambda t: engine_ner.clean_with_gliner(t)),
        ("LLM-Llama3.2", lambda t: engine_llm_pii.clean_with_llm(t, "llama3.2")),
        ("LLM-Mistral", lambda t: engine_llm_pii.clean_with_llm(t, "mistral")),
        ("LLM-Phi3", lambda t: engine_llm_pii.clean_with_llm(t, "phi3"))
    ]

    print(f"{'='*60}")
    print("🚀 INICIANDO TESTE RÁPIDO DE PII (TEXTO CURTO)")
    print(f"{'='*60}")
    print(f"TEXTO ORIGINAL:\n{SAMPLE_TEXT}")
    print(f"{'='*60}\n")

    for name, func in methods:
        print(f"⏳ Executando: {name}...")
        
        start = time.time()
        try:
            result = func(SAMPLE_TEXT)
            duration = time.time() - start
            
            print(f"✅ Finalizado em: {duration:.4f} segundos")
            print(f"RESULTADO:\n{result}")
        except Exception as e:
            print(f"❌ Erro em {name}: {e}")
        
        print(f"{'-'*60}\n")

if __name__ == "__main__":
    run_fast_experiment()