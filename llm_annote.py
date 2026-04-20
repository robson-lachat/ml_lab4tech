# llm_annote.py

import llm_mistral
import llm_openai
import llm_ollama


def annote(text: str, instruction: str, provider: str = "mistral", model: str = None) -> str:
    if not text.strip():
        return "Error: Content text is empty."

    full_prompt = f"INSTRUCTION:\n{instruction}\n\nCONTENT TO ANALYSE:\n{text}"

    try:
        if provider.lower() == "mistral":
            return llm_mistral.send_request(full_prompt)
        if provider.lower() == "openai":
            return llm_openai.send_request(full_prompt)
        if provider.lower() == "ollama":
            # If no template is provided, we use llama3.2 as the default.
            m = model if model else "llama3.2"
            return llm_ollama.send_request(full_prompt, m)
        else:
            return f"Provider {provider} not recognized."
    except Exception as e:
        return f"Error using {provider}: {str(e)}"

if __name__ == "__main__":
    # Fast test: Calling them both in for a comparison!
    text = "The candidate is proficient in Python and Docker."
    obs = "Summarize in one sentence."
    
    print("MISTRAL:", annote(text, obs, "mistral"))
    print("OPENAI :", annote(text, obs, "openai"))