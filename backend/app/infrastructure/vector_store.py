import chromadb
from chromadb.config import Settings
import os
from dotenv import load_dotenv

load_dotenv()

class VectorStoreManager:
    def __init__(self, persist_directory: str = "./chroma_db"):

        host = os.getenv("CHROMA_HOST", "localhost")
        port = int(os.getenv("CHROMA_PORT", "8000"))

        # Inicializa ChromaDB en modo persistente local (gratuito)
        self.client = chromadb.HttpClient(host=host, port=port)
        self.collection = self.client.get_or_create_collection(name="bids_collection")

    def add_document_chunk(self, doc_id: str, text: str, metadata: dict):
        """Almacena un fragmento de texto con sus metadatos y su embedding automático."""
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )

    def search_relevant_context(self, query: str, n_results: int = 3):
        """Busca los fragmentos más relevantes basados en similitud semántica (RAG)."""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results.get("documents", [[]])[0]