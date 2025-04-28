import os
from dotenv import load_dotenv

# Explicit path to .env
from pathlib import Path
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

# Print to verify
openai_key = os.getenv("OPENAI_API_KEY")
mailjet_key = os.getenv("MAILJET_API_KEY")
mailjet_secret = os.getenv("MAILJET_SECRET_KEY")

print("✅ OPENAI_API_KEY:", openai_key[:5] + "..." + openai_key[-4:] if openai_key else "❌ Not Found")
print("📧 MAILJET_API_KEY:", mailjet_key[:5] + "..." + mailjet_key[-4:] if mailjet_key else "❌ Not Found")
print("📧 MAILJET_SECRET_KEY:", mailjet_secret[:5] + "..." + mailjet_secret[-4:] if mailjet_secret else "❌ Not Found")