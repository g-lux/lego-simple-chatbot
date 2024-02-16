from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv  
import streamlit as st  
import os

# Load environment variables from .env file  
load_dotenv()

# Function to load OpenAI model and get response  
def get_openai_response(question):  
    llm = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model_name="gpt-3.5-turbo", temperature=0.6)  
    response = llm.predict(question)  
    return response

# Initialize Streamlit app  
st.set_page_config(page_title="Lego Simple Chatbot", page_icon=":robot_face:", layout="centered")

st.header("Lego Langchain Chatbot Application")

input=st.text_input("Input: ", key="input")  

submit=st.button("Ask the question")

if submit and input:  # ensure input is not empty
    response=get_openai_response(input)
    st.write(response)