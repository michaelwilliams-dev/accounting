import numpy as np
import os
import glob
import pickle
import faiss
from dotenv import load_dotenv
import openai
from tqdm import tqdm

# Load environment
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Settings
data_folder = "data"
index_folder = "faiss_index"
embedding_model = "text-embedding-ada-002"

# Create folders if needed
os.makedirs(index_folder, exist_ok=True)

# Lists to store embeddings and metadata
texts = []
metadatas = []

# Helper to read text and tags
def load_text_and_tags(text_path):
    base = text_path[:-4]  # remove ".txt"
    tagged_path = f"{base}_tagged.txt"
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    if os.path.exists(tagged_path):
        with open(tagged_path, "r", encoding="utf-8") as f:
            tags = f.read().strip()
    else:
        tags = ""
    return text, tags

# Load all files
text_files = glob.glob(os.path.join(data_folder, "*.txt"))
text_files = [f for f in text_files if not f.endswith("_tagged.txt")]  # Exclude the _tagged files

print(f"Found {len(text_files)} text files to index.")

for file_path in tqdm(text_files, desc="Embedding files"):
    text, tags = load_text_and_tags(file_path)
    if not text:
        continue  # Skip empty texts

    try:
        response = openai.Embedding.create(
            input=text,
            model=embedding_model
        )
        embedding = response["data"][0]["embedding"]
        texts.append(embedding)
        metadatas.append({
            "file_name": os.path.basename(file_path),
            "tags": tags
        })
    except Exception as e:
        print(f"⚠️ Error embedding {file_path}: {e}")

# Create FAISS index
dimension = len(texts[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(texts).astype('float32'))
faiss.write_index(index, "embedding/faiss_index")

# Save FAISS index
faiss.write_index(index, os.path.join(index_folder, "index.faiss"))

# Save metadata
with open(os.path.join(index_folder, "metadata.pkl"), "wb") as f:
    pickle.dump(metadatas, f)

print(f"✅ Finished building FAISS index with {len(texts)} entries.")
