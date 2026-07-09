from pydantic import BaseModel
from fastapi import FastAPI
from .rag.chain import rag_chain

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
