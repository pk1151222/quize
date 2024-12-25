from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from handlers.quiz import start_quiz
from handlers.user_quiz import create_quiz
from handlers.score import view_scores
from handlers.settings import language, set_language
from handlers.report import generate_report

# Load Bot Token from Config
from config.settings import BOT_TOKEN

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command Handlers
    dp.add_handler(CommandHandler("start", start_quiz))
    dp.add_handler(CommandHandler("create_quiz", create_quiz))
    dp.add_handler(CommandHandler("scores", view_scores))
    dp.add_handler(CommandHandler("language", language))

    # Callback Handlers
    dp.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))
    dp.add_handler(CommandHandler("generate_report", generate_report))

    # Start Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
