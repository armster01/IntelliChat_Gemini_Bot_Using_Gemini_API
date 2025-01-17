import streamlit as st

def render_sidebar():
    """Render the sidebar with controls and information"""
    with st.sidebar:
        st.title("🤖 Enhanced Gemini Chat")
        st.markdown("""
        ### About
        An advanced chat interface powered by Google's Gemini AI.
        
        ### Features
        - Natural conversations
        - Markdown support
        - Persistent chat history
        - Enhanced error handling
        - Configurable settings
        """)
        
        # Temperature slider
        temperature = st.slider(
            "Response Creativity",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Higher values make responses more creative but less focused"
        )
        
        # Clear chat button
        if st.button("Clear Chat History", type="primary"):
            st.session_state.messages = []
            st.rerun()
            
        return temperature

def render_chat_interface():
    """Render the main chat interface"""
    st.markdown("### Chat with Enhanced Gemini AI")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "timestamp" in message:
                st.caption(f"Sent at: {message['timestamp']}")