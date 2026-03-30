import google.generativeai as genai
from typing import List

class ResponseGenerator:
    """Handles Stage 7 & 8: Response Generation and Hallucination Control."""
    
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate_response(self, query: str, context_chunks: List[str]) -> str:
        if not context_chunks:
            return "The information is not available in the provided documents."

        context_text = "\n\n---\n\n".join(context_chunks)
        
        prompt = f"""
        You are a strict, factual assistant. Answer the user's question ONLY using the provided context. 
        Do not use outside knowledge. If the answer cannot be found in the context, output exactly: 
        "The information is not available in the provided documents."
        
        Context:
        {context_text}
        
        Question: {query}
        """
        
        response = self.model.generate_content(prompt)
        return response.text
