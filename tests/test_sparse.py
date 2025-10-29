def test_sparse_search():
    from backend.models.sparse_retriever import SparseRetriever
    sr = SparseRetriever()
    docs = ["this is a test", "another document"]
    sr.fit(docs, ids=["1","2"])
    res = sr.search("test", top_k=2)
    assert isinstance(res, list)
