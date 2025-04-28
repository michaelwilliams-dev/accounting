import faiss
import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index and associated metadata
index_path = "faiss_index.index"
data_path = "index_metadata.pkl"

if not os.path.exists(index_path) or not os.path.exists(data_path):
    raise FileNotFoundError("Index or metadata file not found. Please run rebuild_index.py first.")

index = faiss.read_index(index_path)
with open(data_path, "rb") as f:
    metadata = pickle.load(f)

# Query loop
print("🔍 Ready to query the index. Type your question and press Enter (or 'exit' to quit).")
while True:
    query = input("\n❓ Your query: ")
    if query.lower() in ["exit", "quit"]:
        break

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding).astype("float32"), k=5)

    print("\n📄 Top results:")
    for i, idx in enumerate(I[0]):
        print(f"\nResult {i+1}:")
        print("File:", metadata[idx]["filename"])
        print("Chunk:", metadata[idx]["chunk"])
        print("Tags:", ", ".join(metadata[idx].get("tags", [])))
