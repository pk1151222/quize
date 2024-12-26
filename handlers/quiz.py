from telegram import Update
from telegram.ext import ContextTypes
from utils.helper import load_language
from database.models import get_quiz_questions

async def handle_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    language = load_language(user_id)
    questions = get_quiz_questions()

    if not questions:
        await update.callback_query.message.reply_text(language["no_quiz_available"])
        return

    # Send first question
    question = questions[0]
    keyboard = [[InlineKeyboardButton(opt, callback_data=f"answer_{idx}") for idx, opt in enumerate(question["options"])]]
    await update.callback_query.message.reply_text(
        language["question_prompt"].format(question=question["text"]),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
