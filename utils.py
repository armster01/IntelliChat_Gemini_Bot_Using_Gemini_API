import streamlit as st
import google.generativeai as genai
from config import Config

def initialize_gemini():
    """Initialize Gemini API and model"""
    genai.configure(api_key=Config.GEMINI_API_KEY)
    return genai.GenerativeModel(Config.MODEL_NAME)

def initialize_session_state():
    """Initialize or reset session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

def format_message(text, role="user"):
    """Format message for chat history"""
    return {
        "role": role,
        "content": text,
        "timestamp": st.session_state.get("current_time", "")
    }

def clear_chat_history():
    """Clear chat history and reset session state"""
    st.session_state.messages = []
    st.session_state.conversation = None
    st.rerun()