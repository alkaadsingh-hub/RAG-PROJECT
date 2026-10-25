import chromadb
from chromadb.config import Settings

# ✅ Create / Load persistent DB
def get_collection():
    client = chromadb.Client(
        Settings(
            persist_directory="chroma_db"
        )
    )

    collection = client.get_or_create_collection("pdf_data")
    return client, collection


# ✅ Store embeddings (used in ingestion phase)
def store_embeddings(embedded_docs):
    client, collection = get_collection()

    print("Storing embeddings...")  # 👈 DEBUG

    for i, doc in enumerate(embedded_docs):
        collection.add(
            ids=[str(i)],
            documents=[doc["content"]],
            embeddings=[doc["embedding"]],
            metadatas=[doc["metadata"]]
        )

    print("Storing embeddings...")  # 👈 DEBUG

   