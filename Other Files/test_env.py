import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

if key:
    print("✅ OPENAI_API_KEY loaded successfully.")
    print(f"Key starts with: {key[:10]}...")
else:
    print("❌ Failed to load OPENAI_API_KEY.")
