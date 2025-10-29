import os
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except Exception:
    SentenceTransformer = None

class DenseRetriever:
    def __init__(self, model_name=None):
        self.model_name = model_name
        self.model = None
        if SentenceTransformer and model_name:
            try:
                self.model = SentenceTransformer(model_name)
            except Exception:
                self.model = None

    def embed(self, texts):
        if self.model:
            return self.model.encode(texts, show_progress_bar=False)
        # fallback: random vectors (placeholder)
        return np.random.randn(len(texts), 384)

    def index(self, embeddings, ids):
        # placeholder: vector store handled elsewhere
        pass

    def search_embeddings(self, query_embedding, top_k=5, vector_store=None):
        # vector_store expected to implement search(embedding, k)
        if vector_store:
            return vector_store.search(query_embedding, k=top_k)
        return []
