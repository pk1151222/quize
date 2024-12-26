from telegram import Update
from telegram.ext import ContextTypes
from database.models import save_user_quiz

async def create_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    quiz_data = context.user_data.get("quiz_data", {})

    if "title" not in quiz_data:
        quiz_data["title"] = update.message.text
        await update.message.reply_text("Enter the first question:")
    else:
        question = update.message.text
        quiz_data["questions"].append({"text": question, "options": [], "answer": None})
        await update.message.reply_text("Enter options separated by commas:")

    context.user_data["quiz_data"] = quiz_data
    save_user_quiz(user_id, quiz_data)
