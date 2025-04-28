# evaluate_index.py

import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Settings
INDEX_PATH = "faiss_index.index"
MAPPING_PATH = "faiss_mapping.pkl"
EVAL_PATH = "evaluation_set.txt"  # Each line: query || expected_keyword

# Load model and FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)

with open(MAPPING_PATH, "rb") as f:
    mapping = pickle.load(f)

# Load evaluation queries
with open(EVAL_PATH, "r") as f:
    eval_pairs = [line.strip().split("||") for line in f if "||" in line]

# Evaluate
top_k = 5
hits = 0

print("\n🧪 Evaluation Results:\n")

for query, expected in eval_pairs:
    query_embedding = model.encode([query])
    scores, indices = index.search(query_embedding, top_k)
    retrieved = [mapping[i].lower() for i in indices[0]]

    match = any(expected.lower() in doc for doc in retrieved)
    result = "✅" if match else "❌"
    if match:
        hits += 1

    print(f"{result} Query: '{query.strip()}' | Expected: '{expected.strip()}'")

# Summary
print(f"\n📊 Accuracy: {hits}/{len(eval_pairs)} correct ({(hits/len(eval_pairs)) * 100:.2f}%)")