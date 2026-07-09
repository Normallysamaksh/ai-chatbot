from .loader import load_documents
from .splitter import split_documents
from .vector_store import vector_store


def ingest_documents(file_paths: list[str]):
    documents = load_documents(file_paths)
    chunks = split_documents(documents)
    vector_store.add_documents(chunks)


if __name__ == "__main__":
    ingest_documents([
        "backend/uploads/advice.pdf",
    ])
