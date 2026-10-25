

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunked_docs = []

    for doc in docs:
        chunks = splitter.split_text(doc["content"])

        for chunk in chunks:
            chunked_docs.append({
                "content": chunk,
                "metadata": doc["metadata"]
            })

    return chunked_docs