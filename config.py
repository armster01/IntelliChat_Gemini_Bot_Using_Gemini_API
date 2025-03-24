import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration class
class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.0-pro-exp-02-05"
    IMAGE_MODEL_NAME = "gemini-pro-vision"
    
    # Streamlit configs
    PAGE_TITLE = "Enhanced Gemini Chat"
    PAGE_ICON = "🤖"
    LAYOUT = "wide"
    
    # Chat settings
    MAX_HISTORY = 100
    DEFAULT_TEMPERATURE = 0.7
