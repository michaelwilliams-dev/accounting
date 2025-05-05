
import json, os

with open("data/accounting/accounting_metadata.json") as f:
    metadata = json.load(f)

missing = []
for k, entry in metadata.items():
    filename = entry["chunk_file"]
    if not os.path.exists(f"data/accounting/{filename}"):
        missing.append(filename)

print(f"🔍 Missing {len(missing)} chunk files:")
for name in missing:
    print(f"  ❌ {name}")