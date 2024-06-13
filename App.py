# chat.py

# Import necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API key for Google Gemini Pro
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """
    Function to get response from Gemini Pro model based on user input.
    """
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit application
st.set_page_config(page_title="Chatbot")
st.header("TharapEase: Your Mental Wellness Ally")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input field and submit button
input_text = st.text_input("Input:", key="input")
submit_button = st.button("Ask the question")

# Process user input and generate response
if submit_button and input_text:
    response = get_gemini_response(input_text)
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("Chat History:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
