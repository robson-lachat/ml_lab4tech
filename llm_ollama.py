import os
from openai import OpenAI

# Ollama runs on port 11434 by default.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" # Dummy key required by lib
)

def send_request(full_prompt: str, model_name: str) -> str:
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response.choices[0].message.content