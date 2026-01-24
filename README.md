# DocuMind RAG

DocuMind RAG is a Retrieval-Augmented Generation (RAG) system that enables document-grounded question answering using Large Language Models (LLMs). Instead of generating answers from general knowledge, the system retrieves semantically relevant information from user-provided documents and uses it as context for response generation, significantly reducing hallucination.

---

## Features

- Upload PDF documents
- Semantic search over document content using embeddings
- Vector database–backed retrieval
- Context-aware question answering
- Reduced hallucination through document grounding
- Graceful handling of unknown queries when information is not present in the document

---

## System Overview

Traditional LLM-based chatbots rely solely on pre-trained knowledge and may generate incorrect or fabricated answers. DocuMind RAG addresses this limitation by combining information retrieval with text generation.

### High-level workflow

1. User uploads a PDF document  
2. Text is extracted and split into manageable chunks  
3. Each chunk is converted into a vector embedding  
4. Embeddings are stored in a vector database  
5. User submits a question  
6. Relevant document chunks are retrieved using semantic similarity  
7. Retrieved context is passed to the LLM  
8. The LLM generates a response grounded in the document content  

---

## Tech Stack

- Backend: Python, FastAPI  
- LLM: OpenAI or compatible LLM API  
- Embeddings: Sentence Transformers  
- Vector Database: FAISS  
- Document Processing: PyPDF2  
- API Server: Uvicorn  

---

## Project Structure

```text
documind-rag/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── upload.py
│   │   │   └── query.py
│   │   ├── services/
│   │   │   ├── pdf_loader.py
│   │   │   ├── chunker.py
│   │   │   ├── embeddings.py
│   │   │   ├── vector_store.py
│   │   │   └── rag.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── prompts.py
│   │   └── models/
│   │       └── schemas.py
│   └── requirements.txt
├── data/
│   └── documents/
├── README.md
└── .gitignore
```


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/documind-rag.git
cd documind-rag
```

### 2. Create and activate a virtual environment

Create the virtual environment:
```bash

python -m venv venv
```
Activate it on macOS / Linux:
```bash

source venv/bin/activate
```
Activate it on Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash

pip install -r backend/requirements.txt
```
### 4. Run the backend server
```bash
uvicorn backend.app.main:app --reload
```
Once the server is running, the API will be available at:
```bash
http://127.0.0.1:8000
```

---

## API Endpoints (Initial)

- POST `/upload`  
  Upload PDF documents

- POST `/query`  
  Ask questions based on uploaded documents

API details will evolve as the project progresses.

---

## Limitations

- Performance depends on document quality and chunking strategy  
- Documents must be reprocessed when updated  
- Designed for small-to-medium document collections  

---

## Project Objective

The primary objective of this project is to demonstrate how Retrieval-Augmented Generation can be used to build reliable, domain-specific AI systems by grounding LLM outputs in external knowledge sources.

---

## Future Enhancements

- Support for multiple documents  
- Improved chunking strategies  
- Frontend user interface for document upload and chat  
- Metadata-based filtering  
- Containerized deployment using Docker  

---

## Contributors

- Backend, RAG Pipeline and Integration: Venkata Pavan Kumar Utpala
- Frontend: Anusha Mittal  

---

## License

This project is developed for academic purposes.




