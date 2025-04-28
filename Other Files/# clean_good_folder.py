# clean_good_folder.py

import os
import shutil

# Paths
good_folder = "data_clean/good"
bad_folder = "data_clean/bad_in_good"

# Make sure the bad folder exists
os.makedirs(bad_folder, exist_ok=True)

# Keywords that show the file is bad
error_keywords = ["Error", "Failed", "Incorrect API key", "Unauthorized", "error code"]

# Scan through the files
for filename in os.listdir(good_folder):
    file_path = os.path.join(good_folder, filename)

    if os.path.isfile(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            # Check if content is bad
            if (
                len(content) < 50  # very small file
                or any(keyword.lower() in content.lower() for keyword in error_keywords)
            ):
                print(f"🚮 Moving bad file: {filename}")
                shutil.move(file_path, os.path.join(bad_folder, filename))

        except Exception as e:
            print(f"❌ Failed checking {filename}: {e}")

print("✅ Good folder cleaned up.")