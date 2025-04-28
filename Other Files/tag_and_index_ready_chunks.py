import os

# Optional: Load API keys if needed
from dotenv import load_dotenv
load_dotenv()

# Set your data folder
data_folder = "data"

# Loop through all files in the data folder
for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)

    # Only process files, skip folders
    if os.path.isfile(file_path):
        print(f"\n📄 Processing: {filename}")

        try:
            # Read file in binary mode and decode safely
            with open(file_path, "rb") as f:
                content = f.read()

            text = content.decode("utf-8", errors="ignore")

            # Dummy "tagging" logic (replace with your real tagging/indexing)
            print(f"✅ {filename} - {len(text)} characters loaded")
            # Example: print first chunk
            print(f"🔹 Sample content:\n{text[:300]}...\n")

            # TODO: Call your tag_chunk(text) and index logic here

        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")