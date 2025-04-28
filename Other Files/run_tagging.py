import os
from tagged import tag_chunk

input_folder = "data"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt") and not filename.endswith("_tagged.txt"):
        filepath = os.path.join(input_folder, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        print(f"🔍 Tagging: {filename}")
        tagged_text = tag_chunk(content)

        tagged_filename = filename.replace(".txt", "_tagged.txt")
        tagged_filepath = os.path.join(input_folder, tagged_filename)
        with open(tagged_filepath, "w", encoding="utf-8") as f:
            f.write(tagged_text)
        print(f"✅ Saved: {tagged_filename}")