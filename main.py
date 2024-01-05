import streamlit as st
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-pro')



if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.set_page_config(page_title="Chat with Gemini Pro", page_icon=":robot")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Chat With *Gemini-Pro*")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role
    

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)


if prompt := st.chat_input("ASK ME ANYTHING YOU WANT"):
    st.chat_message("user").markdown(prompt)
    response= st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)


        
