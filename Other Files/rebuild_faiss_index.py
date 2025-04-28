import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Directory containing the tagged text files
tagged_folder = "data"
index_file = "faiss_index/index.faiss"
meta_file = "faiss_index/metadata.pkl"

# Ensure index folder exists
os.makedirs("faiss_index", exist_ok=True)

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Store metadata (filename and text content)
metadata = []
texts = []

print("🔍 Scanning for tagged files...")
for filename in os.listdir(tagged_folder):
    if filename.endswith("_tags_tagged.txt"):
        filepath = os.path.join(tagged_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            texts.append(content)
            metadata.append({"filename": filename, "content": content[:200]})
            print(f"✅ Loaded: {filename}")

print("🧠 Encoding texts...")
embeddings = model.encode(texts, show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, index_file)
with open(meta_file, "wb") as f:
    pickle.dump(metadata, f)

print(f"✅ FAISS index saved to {index_file}")
print(f"🗂️ Metadata saved to {meta_file}")
