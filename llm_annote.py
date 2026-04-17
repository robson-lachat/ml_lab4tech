import llm_mistral
import llm_openai

def annote(text: str, instruction: str, provider: str = "mistral") -> str:
    if not text.strip():
        return "Error: Content text is empty."

    full_prompt = f"INSTRUCTION:\n{instruction}\n\nCONTENT TO ANALYSE:\n{text}"

    try:
        if provider.lower() == "mistral":
            return llm_mistral.send_request(full_prompt)
        elif provider.lower() == "openai":
            return llm_openai.send_request(full_prompt)
        else:
            return f"Provider {provider} not recognized."
    except Exception as e:
        return f"Error using {provider}: {str(e)}"

if __name__ == "__main__":
    # Fast test: Calling them both in for a comparison!
    texto = "The candidate is proficient in Python and Docker."
    obs = "Summarize in one sentence."
    
    print("MISTRAL:", annote(texto, obs, "mistral"))
    print("OPENAI :", annote(texto, obs, "openai"))