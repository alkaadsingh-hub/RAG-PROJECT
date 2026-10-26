# 📄 RAG-Based Document Question Answering System

## 📌 About the Project
This project is an AI-powered document question-answering system built using **Retrieval-Augmented Generation (RAG)**. It extracts information from PDF documents, processes the content, stores embeddings in a vector database, and generates relevant answers to user queries using an LLM.

## 🚀 Features
- PDF text extraction and document processing
- Table extraction from PDF files
- Text chunking for efficient retrieval
- Embedding generation for semantic search
- Vector storage and retrieval using ChromaDB
- AI-generated answers using Google Gemini
- Interactive user interface built with Streamlit

## 🛠️ Tech Stack
- **Language:** Python
- **LLM:** Google Gemini
- **Framework:** Streamlit, LangChain
- **Vector Database:** ChromaDB
- **PDF Processing:** PyMuPDF (fitz), pdfplumber
- **Other Tools:** Python dotenv, Tabulate

## ⚙️ How It Works

1. **Document Upload:** Input PDF documents.
2. **Data Extraction:** Extract text, images, and tables.
3. **Text Chunking:** Split text into smaller chunks.
4. **Embeddings:** Convert chunks into vector representations.
5. **Vector Storage:** Store embeddings in ChromaDB.
6. **Retrieval:** Find relevant document chunks for a query.
7. **Answer Generation:** Use Gemini to generate answers based on retrieved context.

## 📂 Project Structure

```text
RAG-Project/
│
├── app.py          # Streamlit application
├── parser.py       # Extract text and images
├── tables.py       # Extract tables from PDFs
├── chunking.py     # Split text into chunks
├── embeddings.py   # Generate embeddings
├── vectordb.py     # Store and retrieve vectors
├── query.py        # Retrieve relevant documents
├── llm.py          # Generate answers using Gemini
├── data/
│   ├── markdown/
│   └── images/
├── .env            # API key configuration
└── requirements.txt
```

## 💻 Installation and Setup

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd RAG-Project
```

**2. Create a virtual environment**

```bash
py -m venv venv
```

**3. Activate the environment (Windows)**

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Install dependencies**

```bash
py -m pip install -r requirements.txt
```

**5. Configure the API key**

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

**6. Run the application**

```bash
py -m streamlit run app.py
```

## 🎯 Learning Outcomes
- Understanding Large Language Models (LLMs)
- Implementing Retrieval-Augmented Generation
- Working with text embeddings and vector databases
- Processing PDFs and extracting structured information
- Building interactive AI applications using Streamlit

## 🔮 Future Improvements
- Support for multiple document formats
- Improved retrieval accuracy and evaluation
- Source citations in generated answers
- OCR support for scanned documents
- Deployment as a production-ready AI application
