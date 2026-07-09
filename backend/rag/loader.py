from pathlib import Path
from langchain_community.document_loaders import (
    UnstructuredWordDocumentLoader,
    PyPDFLoader,
    TextLoader,
)

LOADERS = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
    ".docx": UnstructuredWordDocumentLoader,
}


def load_document(file_path: str):
    path = Path(file_path)

    extension = path.suffix.lower()
    if extension not in LOADERS:
        raise ValueError(f"Incorrect document format: {extension}")

    loader = LOADERS[extension](str(path))
    return loader.load()


def load_documents(file_paths: list[str]):
    documents = []

    for file_path in file_paths:
        documents.extend(load_document(file_path))

    return documents
