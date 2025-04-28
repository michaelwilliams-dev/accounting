import os
from dotenv import load_dotenv

load_dotenv()

def load_chunks_from_folder(folder_path):
    chunks = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                chunks.append(file.read())
    return chunks

# Path to your chunk folder
folder_path = os.path.expanduser("~/Documents/accounting_c_txt")

# Load the chunks
chunks = load_chunks_from_folder(folder_path)
print(f"Loaded {len(chunks)} chunks.")