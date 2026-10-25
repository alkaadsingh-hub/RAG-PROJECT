from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(query, documents, metadatas):
    context = ""

    for doc, meta in zip(documents, metadatas):
        context += f"\n[Page {meta.get('page')} | {meta.get('type')}]\n{doc}\n"

    prompt = f"""
You are a highly accurate assistant.

Answer ONLY using the context below.
Do NOT guess.
If answer is not found, say: "Not found in document."

Give clear and structured answers.

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

