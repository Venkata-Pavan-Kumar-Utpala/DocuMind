import PyPDF2
from typing import IO

class DocumentIngestor:
    """Handles Stage 1: Document Ingestion."""
    
    @staticmethod
    def extract_text(pdf_file: IO[bytes]) -> str:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text