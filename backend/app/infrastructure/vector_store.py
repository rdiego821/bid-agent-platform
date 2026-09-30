import chromadb
from chromadb.config import Settings
import os

class VectorStoreManager:
    def __init__(self, persist_directory: str = "./chroma_db"):
        # Inicializa ChromaDB en modo persistente local (gratuito)
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name="bids_collection")

    def add_document(self, doc_id: str, text: str, metadata: dict):
        """Agrega un fragmento de documento al almacén vectorial."""
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )

    def search_similar(self, query: str, n_results: int = 3):
        """Busca fragmentos relevantes similares a una consulta."""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results