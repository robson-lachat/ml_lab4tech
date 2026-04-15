from mistralai.client import Mistral
import os

#api_key = os.environ["MISTRAL_API_KEY"]
api_key = 
model="mistral-small-latest"

client = Mistral(api_key=api_key)

def annote(text: str) -> str:
    #Recive CV text    

    if not text.strip():
        return "Error: Not find text. PDF empty."

    prompt = f"""
    Analyze this CV and answer:

    1. What are the main skills?
    2. What is the experience level?
    3. What are strengths and weaknesses?

    CV TEXT:
    {text}
    """

    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Error to call Mistral: {e}"

# O bloco abaixo serve apenas para testes rápidos deste arquivo isolado
if __name__ == "__main__":
    test_text = "Experience: 5 years as Python Developer. Skills: Docker, AWS, Java."
    print(annote(test_text))