import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict

class VectorStore:
    """Handles Stage 3 & 4: Embedding and Storage."""
    
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.encoder = SentenceTransformer(model_name)
        self.dimension = self.encoder.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatIP(self.dimension)
        self.chunk_map: Dict[int, str] = {}
        self.current_id = 0

    def embed_and_store(self, chunks: List[str]) -> None:
        if not chunks:
            return
            
        embeddings = self.encoder.encode(chunks, normalize_embeddings=True)
        self.index.add(np.array(embeddings, dtype=np.float32))
        
        for chunk in chunks:
            self.chunk_map[self.current_id] = chunk
            self.current_id += 1