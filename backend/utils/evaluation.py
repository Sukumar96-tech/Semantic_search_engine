from typing import List, Dict

def precision_at_k(retrieved: List, relevant_ids: set, k: int) -> float:
    if k == 0:
        return 0.0
    topk = retrieved[:k]
    hits = sum(1 for r in topk if r.get("id") in relevant_ids)
    return hits / k

def mean_average_precision(all_retrieved: List[List[Dict]], all_relevant: List[set]) -> float:
    # Placeholder for batch MAP computation
    return 0.0
