import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
mailjet_api = os.getenv("MAILJET_API_KEY")
mailjet_secret = os.getenv("MAILJET_SECRET_KEY")

print("🔑 OPENAI_API_KEY:", openai_key[:5] + "..." + openai_key[-4:] if openai_key else "❌ Not Found")
print("📧 MAILJET_API_KEY:", mailjet_api[:5] + "..." + mailjet_api[-4:] if mailjet_api else "❌ Not Found")
print("📧 MAILJET_SECRET_KEY:", mailjet_secret[:5] + "..." + mailjet_secret[-4:] if mailjet_secret else "❌ Not Found")