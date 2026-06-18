# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from rag import rag_retrieve

app = FastAPI(title="RAG API")

class Query(BaseModel):
    question: str

@app.post("/rag")
def ask_rag(query: Query):
    answer = rag_retrieve(query.question)
    return {'answer': answer}
