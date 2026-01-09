import os

def load_text(text_or_path: str) -> str:
    if os.path.exists(text_or_path):
        with open(text_or_path, "r", encoding="utf-8") as f:
            return f.read()
    return text_or_path
