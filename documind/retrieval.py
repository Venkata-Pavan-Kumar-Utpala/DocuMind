import numpy as np
from typing import List
from .storage import VectorStore

class Retriever:
    """Handles Stage 5 & 6: Query Handling and Retrieval."""
    
    def __init__(self, vector_store: VectorStore, top_k: int = 3, threshold: float = 0.3):
        self.vector_store = vector_store
        self.top_k = top_k
        self.threshold = threshold

    def retrieve(self, query: str) -> List[str]:
        query_vector = self.vector_store.encoder.encode([query], normalize_embeddings=True)
        distances, indices = self.vector_store.index.search(np.array(query_vector, dtype=np.float32), self.top_k)
        
        relevant_chunks = []
        for i in range(self.top_k):
            if distances[0][i] >= self.threshold and indices[0][i] != -1:
                relevant_chunks.append(self.vector_store.chunk_map[indices[0][i]])
                
        return relevant_chunks