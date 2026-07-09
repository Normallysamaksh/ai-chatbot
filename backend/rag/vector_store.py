from pathlib import Path
from langchain_chroma import Chroma
from .embeddings import embeddings

CHROMA_PATH = Path(__file__).parent.parent / "chroma_db"

vector_store = Chroma(
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings,
)
