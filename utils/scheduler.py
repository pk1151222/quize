from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
from config.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

def send_reminder():
    bot.send_message(chat_id=user_id, text="Don't forget to play a quiz today!")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_reminder, 'interval', hours=24)
    scheduler.start()
