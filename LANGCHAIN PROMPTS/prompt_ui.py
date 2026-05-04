from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

st.header("Reasearch Tool")

user_input=st.text_input("enter your Prompt")

if st.button("summarize"):
    res=model.invoke(user_input)
    st.write(res.content)