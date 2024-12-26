import json

def load_language(user_id):
    # Load user language (default to English)
    lang = "en"  # Replace with actual logic to fetch user language from DB
    with open(f"languages/{lang}.json", "r", encoding="utf-8") as file:
        return json.load(file)
