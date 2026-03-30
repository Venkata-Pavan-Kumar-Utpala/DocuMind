#  DocuMind RAG

DocuMind RAG is a modular Retrieval-Augmented Generation (RAG) application built with Python and Streamlit. It allows users to upload PDF documents and ask questions about them. The system ensures that all answers are strictly grounded in the uploaded text, utilizing advanced chunking, vector search, and hallucination control mechanisms.

##  Key Features

* **Document Ingestion:** Parses raw text from user-uploaded PDF files.
* **Intelligent Text Processing:** Splits text into manageable chunks with controlled overlap to preserve semantic context across sentence boundaries.
* **Vector Embeddings:** Utilizes the `all-MiniLM-L6-v2` sentence transformer model to convert text chunks into high-quality vector representations.
* **Fast Similarity Search:** Leverages **FAISS** (Facebook AI Similarity Search) for blazing-fast retrieval of the most relevant text chunks based on user queries.
* **Hallucination Control:** Implements strict similarity threshold filtering. If a query falls outside the scope of the document, the system safely defaults to: *"The information is not available in the provided documents."*
* **Generative AI Integration:** Powered by Google's **Gemini 2.5 Flash** model to synthesize retrieved context into clear, conversational answers.

##  Technology Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **PDF Extraction:** [PyPDF2](https://pypdf2.readthedocs.io/)
* **Embeddings:** [Sentence-Transformers](https://sbert.net/) (`all-MiniLM-L6-v2`)
* **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss) (CPU)
* **LLM:** [Google Generative AI](https://aistudio.google.com/) (`gemini-2.5-flash`)

##  Installation and Setup

Follow these steps to run the project on your local machine.

### 1. Prerequisites
* Python 3.8 or higher installed on your system.
* A free [Google Gemini API Key](https://aistudio.google.com/).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME
```
### 3. Set Up a Virtual Environment
It is highly recommended to run this project inside a virtual environment.

For Windows:

```DOS
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux:

```Bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```Bash
pip install -r requirements.txt
```

##  Running the Application
Once your dependencies are installed and your virtual environment is active, launch the app with:

```Bash
streamlit run app.py
```
The application will open automatically in your default web browser at http://localhost:8501.

## 📖 How to Use
- Enter API Key: Paste your Gemini API key into the secure sidebar input.

- Upload Document: Use the file uploader to provide a PDF. Wait for the success message confirming the document has been processed and vectorized.

- Query: Type a question related to the document in the main chat interface.

- Explore: Read the generated answer and expand the "View Retrieved Context" section to see the exact text chunks the system used to formulate its response.

#  Project Structure

```plaintext
documind_rag/
├── app.py                  # Main Streamlit frontend interface
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── documind/               # Backend modules
    ├── __init__.py
    ├── ingestion.py        # PDF text extraction
    ├── processing.py       # Text chunking and overlapping
    ├── storage.py          # Embedding generation and FAISS vector store
    ├── retrieval.py        # Query vectorization and similarity search
    └── generation.py       # LLM prompting and hallucination control
```

