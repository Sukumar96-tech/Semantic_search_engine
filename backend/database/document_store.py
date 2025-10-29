import sqlite3
import os
import json

DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./backend/data/documents.db").replace("sqlite://///", "")

class DocumentStore:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._ensure_table()

    def _conn(self):
        return sqlite3.connect(self.db_path)

    def _ensure_table(self):
        conn = self._conn()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            title TEXT,
            text TEXT,
            meta TEXT
        )
        """)
        conn.commit()
        conn.close()

    def add_document(self, doc_id, title, text, meta=None):
        conn = self._conn()
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO documents(id,title,text,meta) VALUES (?,?,?,?)",
                    (str(doc_id), title, text, json.dumps(meta or {})))
        conn.commit()
        conn.close()

    def get_document(self, doc_id):
        conn = self._conn()
        cur = conn.cursor()
        cur.execute("SELECT id,title,text,meta FROM documents WHERE id=?", (str(doc_id),))
        row = cur.fetchone()
        conn.close()
        if not row:
            return None
        return {"id": row[0], "title": row[1], "text": row[2], "meta": json.loads(row[3] or "{}")}\n
    def get_all_documents(self):\n        conn = self._conn()\n        cur = conn.cursor()\n        cur.execute("SELECT id,title,text FROM documents")\n        rows = cur.fetchall()\n        conn.close()\n        return [{"id": r[0], "title": r[1], "text": r[2]} for r in rows]\n