from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставь свой токен от BotFather
TOKEN = "7416695404:AAE18OU0B0BfJf3E8wAFpHo9psJ8TgwBZbg"

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Бот работает!")

# Создаем приложение (новый Updater)
application = Application.builder().token(TOKEN).build()

# Добавляем обработчик команды /start
application.add_handler(CommandHandler("start", start))

# Запуск бота
if __name__ == "__main__":  # ВАЖНО! Два подчеркивания с обеих сторон!
    print("Бот запущен...")
    application.run_polling()