# Semantic Search Engine

Lightweight semantic search scaffold with dense, sparse and hybrid retrievers, a FastAPI backend and a Streamlit frontend.

Features
- FastAPI backend with search and upload endpoints
- Dense retriever (Sentence-BERT) and sparse retriever (TF-IDF) stubs
- Hybrid retriever that combines dense + sparse ranking
- Simple vector store wrapper (FAISS optional)
- Streamlit frontend for interactive search and dataset upload
- Docker compose for local deployment

How to use (quickstart)
1. Create a new repository and add the files from this scaffold.
2. Populate `backend/data/documents.csv` with your dataset (columns: id,title,text).
3. Update `.env` with any API keys / model names if needed.
4. From the project root:
   - Backend (dev): `uvicorn backend.main:app --reload --port 8000`
   - Frontend: `streamlit run frontend/app.py`
5. Or run with Docker Compose:
   - `cd deployment && ./start.sh` (make executable)

Project layout
- backend/ : FastAPI app, models, database, utils
- frontend/: Streamlit UI and API client
- deployment/: Dockerfiles and docker-compose for local deployment
- tests/: basic pytest stubs

Notes
- This scaffold contains minimal retriever implementations for quick prototyping. Replace or tune models and vector stores for production workloads.
- I left TODO markers where you should plug in dataset preprocessing, indexing or model weights.

License
- Add your preferred license file if needed.