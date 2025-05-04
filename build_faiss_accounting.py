import os
import json
import faiss
import numpy as np
from openai import OpenAI

# --- Load OpenAI key from environment ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- CONFIG ---
CHUNK_DIR = "/Users/michaelwilliams/Documents/github/accounting/data/accounting"
INDEX_PATH = os.path.join(CHUNK_DIR, "accounting.index")
METADATA_PATH = os.path.join(CHUNK_DIR, "accounting_metadata.json")
EMBED_MODEL = "text-embedding-3-small"

# --- Collect chunks ---
chunk_files = sorted([
    f for f in os.listdir(CHUNK_DIR)
    if f.endswith(".txt") and "_tagged" not in f
])
print(f"🧩 Found {len(chunk_files)} chunks")

embeddings = []
metadata = {}

# --- Generate embeddings ---
for i, filename in enumerate(chunk_files):
    file_path = os.path.join(CHUNK_DIR, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    try:
        response = client.embeddings.create(
            model=EMBED_MODEL,
            input=[text]
        )
        vector = np.array(response.data[0].embedding, dtype="float32")
        embeddings.append(vector)
        metadata[i] = {
            "chunk_file": filename,
            "tokens": len(text.split()),
        }
        print(f"✅ Embedded: {filename}")

    except Exception as e:
        print(f"❌ Error embedding {filename}: {e}")

# --- Build and save FAISS index ---
if not embeddings:
    print("❌ No embeddings were generated. Check your API key or input files.")
    exit(1)

dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.stack(embeddings))
faiss.write_index(index, INDEX_PATH)
print(f"📦 FAISS index saved to {INDEX_PATH}")

# --- Save metadata ---
with open(METADATA_PATH, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print(f"📝 Metadata saved to {METADATA_PATH}")