def test_hybrid_integration():
    from backend.models.hybrid_retriever import HybridRetriever
    hr = HybridRetriever()
    # With no documents the search should return empty list
    res = hr.search("anything", k=3)
    assert isinstance(res, list)
