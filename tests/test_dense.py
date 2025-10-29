def test_dense_placeholder():
    # Placeholder test: import the DenseRetriever and ensure embed returns shape
    from backend.models.dense_retriever import DenseRetriever
    dr = DenseRetriever()
    vecs = dr.embed(["hello world", "another"])
    assert hasattr(vecs, "__len__")
