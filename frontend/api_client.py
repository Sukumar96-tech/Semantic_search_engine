import requests

class APIClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url.rstrip("/")

    def search(self, query, k=5):
        try:
            resp = requests.post(f"{self.base_url}/search", json={"query": query, "k": k}, timeout=15)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
