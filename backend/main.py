from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

from .config import settings
from .models.hybrid_retriever import HybridRetriever
from .database.init_db import initialize_database

app = FastAPI(title="Semantic Search Engine")

# Initialize components (simple lazy/sync init)
retriever = HybridRetriever()

class SearchRequest(BaseModel):
    query: str
    k: int = 5

@app.on_event("startup")
def startup_event():
    # Initialize DB and optionally index documents (if CSV provided)
    initialize_database()
    retriever.load_or_build_index()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/search")
def search(req: SearchRequest):
    if not req.query:
        raise HTTPException(status_code=400, detail="query is required")
    results = retriever.search(req.query, k=req.k)
    return {"query": req.query, "results": results}

@app.post("/upload")
def upload(data: dict):
    # Minimal passthrough to call DB ingestion (implement complete route if needed)
    # Expect the frontend to call backend/document ingestion endpoint or use CLI script
    return {"status": "not_implemented", "detail": "Use backend.database.init_db to ingest CSV files"}
