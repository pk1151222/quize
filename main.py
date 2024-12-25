from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from handlers.quiz import start_quiz, auto_generate_quiz
from analytics.charts import send_chart
from handlers.score import view_scores
from handlers.report import generate_report
from handlers.settings import language, set_language

from config.settings import BOT_TOKEN
from database.db import setup_db

def main():
    # Set up database tables
    setup_db()

    # Initialize the bot
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command Handlers
    dp.add_handler(CommandHandler("start", start_quiz))
    dp.add_handler(CommandHandler("auto_quiz", auto_generate_quiz))
    dp.add_handler(CommandHandler("scores", view_scores))
    dp.add_handler(CommandHandler("chart", send_chart))
    dp.add_handler(CommandHandler("generate_report", generate_report))
    dp.add_handler(CommandHandler("language", language))

    # Callback Query Handlers
    dp.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
