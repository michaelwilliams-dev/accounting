import os
import json
import faiss
from sentence_transformers import SentenceTransformer

def build_faiss_index_from_chunks(merged_path, index_path, metadata_path):
    # Load merged chunks
    with open(merged_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [entry["text"] for entry in chunks]

    # Generate embeddings
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)

    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, index_path)

    # Save metadata
    metadata = [
        {
            "filename": entry.get("filename", ""),
            "tags": entry.get("tags", []),
            "text": entry["text"]
        }
        for entry in chunks
    ]
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("✅ FAISS index and metadata built and saved.")

# Run this directly for testing
if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    build_faiss_index_from_chunks(
        merged_path=os.path.join(base_path, "data", "merged_chunks.json"),
        index_path=os.path.join(base_path, "data", "accounting_index.index"),
        metadata_path=os.path.join(base_path, "data", "accounting_metadata.json")
    )
