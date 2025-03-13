from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7416695404:AAE18OU0B0BfJf3E8wAFpHo9psJ8TgwBZbg"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Бот работает!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()