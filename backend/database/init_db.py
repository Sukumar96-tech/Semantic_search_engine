import os
import pandas as pd
from ..database.document_store import DocumentStore

DATA_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "documents.csv")

def initialize_database(csv_path: str = None):
    csv_file = csv_path or DATA_CSV
    if not os.path.exists(csv_file):
        return
    df = pd.read_csv(csv_file)
    ds = DocumentStore()
    for _, row in df.iterrows():
        # expect columns: id, title, text
        doc_id = row.get("id") or row.get("doc_id") or _
        title = row.get("title", "")
        text = row.get("text", "")
        ds.add_document(doc_id, title, text)
