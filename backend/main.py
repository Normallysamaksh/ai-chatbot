from pydantic import BaseModel
from fastapi import FastAPI
from .rag.chain import rag_chain
from .rag.ingest import ingest_from_s3

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "API working"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = rag_chain(request.message)

    return {
        "response": answer
    }


@app.post("/ingest")
def ingest():
    ingest_from_s3()
    return {
        "message": "Documents ingested successfully."
    }
