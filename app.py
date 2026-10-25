import streamlit as st
import os

from query import retrieve_docs
from llm import generate_answer
from parser import extract_text_and_images
from tables import extract_tables
from chunking import chunk_text
from embeddings import get_embeddings, embed_query
from vectordb import store_embeddings

st.set_page_config(page_title="PDF RAG Project", layout="wide")

st.title("📄 Welcome to PDF RAG Project")

# -------------------------------
# SESSION STATE (IMPORTANT)
# -------------------------------
if "processed" not in st.session_state:
    st.session_state.processed = False

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# -------------------------------
# INGESTION BUTTON (IMPORTANT FIX)
# -------------------------------
if uploaded_file and st.button("⚙️ Process PDF"):
    os.makedirs("data", exist_ok=True)

    file_path = "temp.pdf"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully")

    with st.spinner("Processing PDF..."):
        # Step 1: Extract text + images
        text_docs = extract_text_and_images(file_path)
        st.write(f"📄 Extracted {len(text_docs)} pages")

        # Step 2: Extract tables
        table_docs = extract_tables(file_path)
        st.write(f"📊 Extracted {len(table_docs)} tables")

        # Combine
        all_docs = text_docs + table_docs

        # Step 3: Chunking (IMPROVED)
        chunked_docs = chunk_text(all_docs)
        st.write(f"✂️ Created {len(chunked_docs)} chunks")

        # Step 4: Embeddings
        embedded_docs = get_embeddings(chunked_docs)
        st.write("🧠 Embeddings generated")

        # Step 5: Store in DB
        store_embeddings(embedded_docs)
        st.write("🗄️ Stored in ChromaDB")

    st.session_state.processed = True
    st.success("🎉 PDF processed successfully!")

# -------------------------------
# QUERY SECTION
# -------------------------------
st.header("💬 Ask Questions from PDF")

user_query = st.text_input("Enter your question")

if user_query:
    if not st.session_state.processed:
        st.warning("⚠️ Please upload and process a PDF first.")
    else:
        with st.spinner("Thinking..."):
            # Embed query
            query_embedding = embed_query(user_query)

            # Retrieve docs (IMPROVED top_k)
            docs, metas = retrieve_docs(query_embedding, top_k=8)

            # Generate answer
            answer = generate_answer(user_query, docs, metas)

        st.subheader("📌 Answer")
        st.write(answer)

        # -------------------------------
        # DEBUG VIEW (VERY IMPORTANT)
        # -------------------------------
        with st.expander("📚 Retrieved Context (Debug)"):
            for i, (doc, meta) in enumerate(zip(docs, metas)):
                st.write(f"### Chunk {i+1}")
                st.write(f"Page: {meta.get('page')} | Type: {meta.get('type')}")
                st.write(doc)
                st.markdown("---")
                

                










