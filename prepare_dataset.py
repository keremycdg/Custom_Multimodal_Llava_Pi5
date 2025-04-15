# prepare_dataset.py
import os
import json

IMAGE_DIR = "images"
TEXT_DIR = "image_descriptions"
OUTPUT_JSON = "images-text/metadata.json"

os.makedirs("images-text", exist_ok=True)

conversations = []

for filename in os.listdir(IMAGE_DIR):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        name = os.path.splitext(filename)[0]
        image_path = os.path.join(IMAGE_DIR, filename)
        text_path = os.path.join(TEXT_DIR, name + ".txt")

        if os.path.exists(text_path):
            with open(text_path, 'r', encoding='utf-8') as f:
                explanation = f.read().strip()

            entry = {
                "image": image_path,
                "conversations": [
                    {"from": "human", "value": "What is shown in this image?"},
                    {"from": "gpt", "value": explanation}
                ]
            }
            conversations.append(entry)

with open(OUTPUT_JSON, 'w', encoding='utf-8') as out:
    json.dump(conversations, out, indent=2)

print(f"Saved {len(conversations)} image-text pairs to {OUTPUT_JSON}")
