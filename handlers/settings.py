import json

def load_language(lang_code):
    try:
        with open(f'languages/{lang_code}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def language(update, context):
    keyboard = [
        [InlineKeyboardButton("English", callback_data="lang_en")],
        [InlineKeyboardButton("हिंदी", callback_data="lang_hi")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please select your language:", reply_markup=reply_markup)

def set_language(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    lang_code = query.data.split("_")[1]

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET language = ? WHERE user_id = ?", (lang_code, user_id))
    conn.commit()
    conn.close()

    translations = load_language(lang_code)
    query.answer(translations.get("language_changed", "Language updated."))
    query.edit_message_text(translations.get("language_changed", "Language updated."))
