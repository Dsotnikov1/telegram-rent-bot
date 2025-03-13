from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os

# Токен бота (берем из переменных окружения)
TOKEN = os.getenv("TOKEN")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Бот работает!")

# Создаем приложение (новый Updater)
application = Application.builder().token(TOKEN).build()

# Добавляем обработчик команды /start
application.add_handler(CommandHandler("start", start))

# Запуск бота
if _name_ == "_main_":
    print("Бот запущен...")
    application.run_polling()