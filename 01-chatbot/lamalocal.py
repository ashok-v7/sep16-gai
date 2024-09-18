from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# 3rd party integration available in langchain_community
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# in list
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)


# streamlit framework

st.title('Langchain Demo With Ollama API')
input_text = st.text_input("Search the topic u want")


# opensource olamaa  LLm -- https://github.com/ollama/ollama
# ollama list
# ollama pull llama3.1
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

# combine all 3
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
