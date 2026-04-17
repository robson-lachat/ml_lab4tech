import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
model = "mistral-small-latest"

def send_request(full_prompt: str) -> str:
    chat_response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": full_prompt}]
    )
    return chat_response.choices[0].message.content