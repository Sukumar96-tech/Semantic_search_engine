from .dense_retriever import DenseRetriever
from .sparse_retriever import SparseRetriever
from ..database.vector_store import VectorStore
from ..database.document_store import DocumentStore

class HybridRetriever:
    def __init__(self, model_name=None):
        self.dense = DenseRetriever(model_name)
        self.sparse = SparseRetriever()
        self.vector_store = VectorStore()
        self.doc_store = DocumentStore()

    def load_or_build_index(self):
        # Load docs from DB
        docs = self.doc_store.get_all_documents()
        if not docs:
            # nothing indexed yet
            return
        texts = [d["text"] for d in docs]
        ids = [d["id"] for d in docs]

        # fit sparse
        self.sparse.fit(texts, ids=ids)

        # optionally load embeddings to vector store (vector_store handles persistence)
        # if embeddings exist in vector_store, keep them; otherwise compute via dense.embed
        # For prototype: compute embeddings and replace store
        embeddings = self.dense.embed(texts)
        self.vector_store.replace(embeddings, ids)

    def search(self, query, k=5):
        # dense search
        q_emb = self.dense.embed([query])[0]
        dense_results = self.vector_store.search(q_emb, k=k)

        # sparse search
        sparse_results = self.sparse.search(query, top_k=k)

        # naive fusion: accumulate scores and return top-k by combined score
        scores = {}
        for r in dense_results:
            scores[r["id"]] = scores.get(r["id"], 0) + (1.0 - r.get("distance", 0))
        for r in sparse_results:
            scores[r["id"]] = scores.get(r["id"], 0) + r.get("score", 0)

        ranked = sorted(scores.items(), key=lambda x: -x[1])[:k]
        results = []
        for doc_id, score in ranked:
            doc = self.doc_store.get_document(doc_id) or {"id": doc_id, "title": "", "text": ""}
            results.append({"id": doc_id, "score": float(score), "title": doc.get("title", ""), "text": doc.get("text", "")})
        return results
