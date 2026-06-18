import streamlit as st
import requests

st.title("RAG Retrieval App")

question = st.text_input("Enter your RAG query")

def get_rag_response(question):
    response = requests.post(
        "http://localhost:8000/rag",
        json={'question':question}
        )
    print(response.json())
    
    return response.json()['answer']

if question:
    st.write(get_rag_response(question))
