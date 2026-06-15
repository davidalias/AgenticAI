import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(".."))
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Respond to the user query"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title("Langchain demo with Openai api")
input_text = st.text_input("Search the topic you want")

#LLM
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))