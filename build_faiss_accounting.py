import os
import json
import faiss
import numpy as np
from openai import OpenAI  # ✅ correct import for SDK v1.77.0

# ✅ use OpenAI client
client = OpenAI(api_key="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")

# --- CONFIG ---
CHUNK_DIR = "/Users/michaelwilliams/Documents/github/accounting/data/accounting"
INDEX_PATH = os.path.join(CHUNK_DIR, "accounting.index")
METADATA_PATH = os.path.join(CHUNK_DIR, "accounting_metadata.json")
EMBED_MODEL = "text-embedding-3-small"

# --- Collect chunks ---
#chunk_files = sorted([f for f in os.listdir(CHUNK_DIR) if f.startswith("chunk_") and f.endswith(".txt")])
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
    with open(os.path.join(CHUNK_DIR, filename), "r", encoding="utf-8") as f:
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
        print(f"✅ {filename} embedded")

    except Exception as e:
        print(f"❌ Error embedding {filename}: {e}")

# --- Build and save FAISS index ---
if not embeddings:
    print("❌ No embeddings were generated. Check your API key or input text.")
    exit(1)
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.stack(embeddings))
faiss.write_index(index, INDEX_PATH)
print(f"📦 FAISS index written to {INDEX_PATH}")

# --- Save metadata ---
with open(METADATA_PATH, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print(f"📝 Metadata saved to {METADATA_PATH}")
