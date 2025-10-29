import os
import numpy as np

try:
    import faiss
    _HAS_FAISS = True
except Exception:
    _HAS_FAISS = False

class VectorStore:
    def __init__(self, dim=384, path=None):
        self.dim = dim
        self.path = path or os.getenv("VECTOR_STORE_PATH", "./backend/data/vector_store.faiss")
        self.ids = []
        self.index = None
        if _HAS_FAISS:
            self.index = faiss.IndexFlatIP(self.dim)

    def replace(self, embeddings, ids):
        embeddings = np.array(embeddings).astype("float32")
        self.ids = list(ids)
        if _HAS_FAISS:
            if embeddings.shape[1] != self.dim:
                # resize dimension
                self.dim = embeddings.shape[1]
                self.index = faiss.IndexFlatIP(self.dim)
            self.index.reset()
            self.index.add(embeddings)
        else:
            # store in-memory fallback
            self._emb = embeddings

    def search(self, query_embedding, k=5):
        if _HAS_FAISS and self.index is not None:
            q = query_embedding.reshape(1, -1).astype("float32")
            scores, idxs = self.index.search(q, k)
            results = []
            for score, idx in zip(scores[0], idxs[0]):
                if idx < 0 or idx >= len(self.ids):
                    continue
                results.append({"id": self.ids[int(idx)], "score": float(score)})
            return results
        else:
            # brute force fallback
            import numpy as np
            dists = (self._emb @ query_embedding).ravel()
            top_idx = (-dists).argsort()[:k]
            return [{"id": self.ids[i], "score": float(dists[i])} for i in top_idx]
