# llm_annote.py

import os
from mistralai.client import Mistral
from dotenv import load_dotenv

# Charge veriable file .env
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
model="mistral-small-latest"

client = Mistral(api_key=api_key)

def annote(text: str, instruction: str) -> str:

    # Receive a personalized text and instruction.    
    if not text.strip():
        return "Error: Content text is empty."

    full_prompt = f"""
    INSTRUCTION:
    {instruction}

    CONTENT TO ANALYSE:
    {text}
    """

    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Error calling Mistral: {e}"

if __name__ == "__main__":
    
    # Isolated test
    text = """
    Michael Johnson is a 34-year-old software developer originally from Brazil, currently living in Lisbon, Portugal.
    He has over 10 years of experience working with Python, data engineering, and cloud platforms such as AWS and Azure.
    João has worked for several international companies, contributing to large-scale data processing systems and machine learning pipelines.
    
    In his free time, he enjoys playing football, reading science fiction books, and experimenting with new programming languages.
    He is also fluent in Portuguese and English, and has an intermediate level in Spanish.
    
    His contact email is joao.silva.dev@example.com and his phone number is +351 912 345 678.
    He recently attended a tech conference in Berlin and is actively looking for new opportunities in Europe.
    """

    prompt = "Extract only the full name of the person mentioned in the text."

    print(annote(text, prompt))