from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database.db import connect_db

def start_quiz(update, context):
    user_id = update.message.from_user.id
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quizzes ORDER BY RANDOM() LIMIT 1")
    quiz = cursor.fetchone()
    conn.close()

    if quiz:
        question, options, answer, difficulty, subject = quiz[1:6]
        options = options.split(",")
        
        keyboard = [
            [InlineKeyboardButton(option, callback_data=f"quiz_{i}") for i, option in enumerate(options)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        context.user_data["quiz_answer"] = answer
        update.message.reply_text(question, reply_markup=reply_markup)
    else:
        update.message.reply_text("No quizzes available!")
