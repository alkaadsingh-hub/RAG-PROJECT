from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_embeddings(chunked_docs):
    embedded_docs = []

    for doc in chunked_docs:
        response = client.models.embed_content(
            model="gemini-embedding-001",  
            contents=doc["content"]
        )

        embedding = response.embeddings[0].values

        embedded_docs.append({
            "embedding": embedding,
            "content": doc["content"],
            "metadata": doc["metadata"]
        })

    return embedded_docs

def embed_query(query):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )
    return response.embeddings[0].values