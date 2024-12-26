from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config.settings import BOT_TOKEN
from handlers.onboarding import start
from handlers.quiz import handle_quiz
from handlers.user_quiz import create_quiz
from handlers.report import generate_report
from handlers.notifications import send_reminders

def main():
    # Initialize the bot
    app = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_quiz, pattern="^quiz_"))
    app.add_handler(CallbackQueryHandler(create_quiz, pattern="^create_quiz$"))
    app.add_handler(CommandHandler("report", generate_report))
    app.add_handler(CommandHandler("reminders", send_reminders))

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
