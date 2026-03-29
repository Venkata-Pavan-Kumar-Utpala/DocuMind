from typing import List

class TextProcessor:
    """Handles Stage 2: Text Processing (Chunking)."""
    
    def __init__(self, chunk_size: int = 500, overlap: int = 75):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str) -> List[str]:
        chunks = []
        start = 0
        text_length = len(text)
        
        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            chunks.append(text[start:end])
            if end == text_length:
                break
            start += self.chunk_size - self.overlap
            
        return chunks