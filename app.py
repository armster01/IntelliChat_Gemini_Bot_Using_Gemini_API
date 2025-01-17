import streamlit as st
from datetime import datetime
from config import Config
from utils import initialize_gemini, initialize_session_state, format_message
from components import render_sidebar, render_chat_interface
from error_handler import handle_errors, ChatError

# Initialize session state and configurations
initialize_session_state()

# Configure page settings
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon=Config.PAGE_ICON,
    layout=Config.LAYOUT
)

# Initialize Gemini
model = initialize_gemini()

@handle_errors
def get_gemini_response(question: str, temperature: float) -> str:
    """Get response from Gemini with error handling"""
    if not question.strip():
        raise ChatError("Please enter a valid question")
    
    response = model.generate_content(
        question,
        generation_config={"temperature": temperature}
    )
    
    if not response.text:
        raise ChatError("Received empty response from Gemini")
    
    return response.text

def main():
    # Render sidebar and get temperature setting
    temperature = render_sidebar()
    
    # Render main chat interface
    render_chat_interface()
    
    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Set current timestamp
        st.session_state.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append(format_message(prompt, "user"))
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt, temperature)
                if response:
                    st.markdown(response)
                    st.session_state.messages.append(
                        format_message(response, "assistant")
                    )

if __name__ == "__main__":
    main()