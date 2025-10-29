import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str = os.getenv("API_KEY", "")
    embedding_model_name: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    vector_store_path: str = os.getenv("VECTOR_STORE_PATH", "./backend/data/vector_store.faiss")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./backend/data/documents.db")

settings = Settings()
