from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from utils.helper import load_language

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    translations = load_language(user_id)

    keyboard = [
        [InlineKeyboardButton(translations["start_quiz"], callback_data="quiz_start")],
        [InlineKeyboardButton(translations["create_quiz"], callback_data="create_quiz")],
    ]

    await update.message.reply_text(
        translations["welcome"],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
