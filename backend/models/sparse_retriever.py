from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class SparseRetriever:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=50000)
        self.doc_vectors = None
        self.ids = []

    def fit(self, docs, ids=None):
        self.ids = ids or list(range(len(docs)))
        self.doc_vectors = self.vectorizer.fit_transform(docs)

    def search(self, query, top_k=5):
        if self.doc_vectors is None:
            return []
        qv = self.vectorizer.transform([query])
        scores = (self.doc_vectors @ qv.T).toarray().ravel()
        top_idx = (-scores).argsort()[:top_k]
        return [{"id": self.ids[i], "score": float(scores[i])} for i in top_idx]
