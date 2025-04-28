import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env variables
load_dotenv()

# Use the API key explicitly if needed
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0,
    openai_api_key=openai_key
)

def tag_chunk(text):
    # example function for testing
    return llm.invoke(text).content