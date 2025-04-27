# view_tags.py

import os
import re

# Set path where _tags.txt files live
TAGS_DIR = "data"

def list_tag_files():
    return [f for f in os.listdir(TAGS_DIR) if f.endswith("_tags.txt")]

def read_tags(filepath):
    with open(os.path.join(TAGS_DIR, filepath), "r") as f:
        return [line.strip() for line in f.readlines()]

def main():
    print("📁 Available tag files:\n")
    files = list_tag_files()
    for i, f in enumerate(files):
        print(f"{i+1}. {f}")
    
    choice = input("\n🔍 Enter file number to view tags or 'search <keyword>': ").strip()

    if choice.startswith("search"):
        _, keyword = choice.split(maxsplit=1)
        print(f"\n🔎 Searching for keyword: '{keyword}'")
        for file in files:
            tags = read_tags(file)
            matches = [tag for tag in tags if keyword.lower() in tag.lower()]
            if matches:
                print(f"\n📄 {file}")
                for tag in matches:
                    print(f"  - {tag}")
    else:
        try:
            idx = int(choice) - 1
            selected_file = files[idx]
            print(f"\n📄 Tags in {selected_file}:\n")
            for tag in read_tags(selected_file):
                print(f"  - {tag}")
        except (IndexError, ValueError):
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()