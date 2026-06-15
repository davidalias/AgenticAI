import os
import sys
sys.path.append(os.path.abspath(".."))

from dotenv import load_dotenv
load_dotenv()  #must be before importing langchain

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn

# FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server"
)

# Base LLM
llm = ChatOpenAI(model="gpt-4o-mini")


# ROUTE 1: Raw OpenAI LLM

add_routes(
    app,
    llm,
    path="/openai"
)


# ROUTE 2: Essay generator

prompt1 = ChatPromptTemplate.from_template(
    "Write an essay about {topic} within 100 words."
)

add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)


# ROUTE 3: Poem generator

prompt2 = ChatPromptTemplate.from_template(
    "Write a poem about {topic} within 100 words."
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)


# Run server

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
