from vectordb import get_collection

def retrieve_docs(query_embedding, top_k=8):
    _, collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return documents, metadatas

