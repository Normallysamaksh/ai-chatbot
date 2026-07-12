from .loader import load_documents
from .splitter import split_documents
from .vector_store import vector_store
from pathlib import Path
from backend.aws.s3 import list_pdfs, download_pdf


def ingest_documents(file_paths: list[str]):
    documents = load_documents(file_paths)
    chunks = split_documents(documents)
    vector_store.add_documents(chunks)


def ingest_from_s3():
    upload_dir = Path("backend/uploads")
    upload_dir.mkdir(exist_ok=True)
    file_paths = []

    for pdf in list_pdfs():
        destination = upload_dir / pdf
        download_pdf(pdf, destination)
        file_paths.append(str(destination))

    ingest_documents(file_paths)


if __name__ == "__main__":
    ingest_from_s3()
