import time
from llm_annote import annote

def run_benchmark():
    test_text = """
    CANDIDATE: Alexandre Silva
    EMAIL: alexandre.silva@email.com
    EXPERIENCE: 5 years of Python development, Docker, and Kubernetes.
    """
    instruction = "Extract the technical skills as a comma-separated list."
    
    # Models on Ollama
    models = ["llama3.2", "mistral", "phi3"]
    
    print(f"{'MODEL':<15} | {'TIME (s)':<10} | {'RESULT'}")
    print("-" * 60)

    for m in models:
        start_time = time.time()
        
        # Calling via Ollama
        response = annote(test_text, instruction, provider="ollama", model=m)
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Cleaning up the response to avoid breaking the table (only take the first line).
        clean_res = response.replace("\n", " ").strip()[:40] + "..."
        
        print(f"{m:<15} | {duration:<10.2f} | {clean_res}")

if __name__ == "__main__":
    run_benchmark()