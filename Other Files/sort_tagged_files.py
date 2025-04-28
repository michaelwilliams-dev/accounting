import os
import shutil

# Paths
data_folder = "data"
good_folder = "data_clean/good"
empty_folder = "data_clean/empty"
original_tags_folder = "data_clean/original_tags"

# Create folders if they don't exist
os.makedirs(good_folder, exist_ok=True)
os.makedirs(empty_folder, exist_ok=True)
os.makedirs(original_tags_folder, exist_ok=True)

for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)

    if filename.endswith("_tags_tagged.txt"):
        # Check if file is empty
        if os.path.getsize(file_path) == 0:
            print(f"🛑 Empty file: {filename}")
            shutil.move(file_path, os.path.join(empty_folder, filename))
        else:
            print(f"✅ Good file: {filename}")
            shutil.move(file_path, os.path.join(good_folder, filename))

    elif filename.endswith("_tags.txt"):
        # Move original tag files separately
        print(f"📦 Moving original tag file: {filename}")
        shutil.move(file_path, os.path.join(original_tags_folder, filename))

print("\n🎯 Done! Files sorted into:")
print(f" - Good files -> {good_folder}")
print(f" - Empty/broken files -> {empty_folder}")
print(f" - Original tags -> {original_tags_folder}")