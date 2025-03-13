from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставь свой токен сюда
TOKEN = "ТВОЙ_ТОКЕН"

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Бот работает!")

# Создаем приложение (новый Updater)
application = Application.builder().token(TOKEN).build()

# Добавляем обработчик команды /start
application.add_handler(CommandHandler("start", start))

# Запуск бота
if name == "__main__":  # Здесь исправлено!
    print("Бот запущен...")
    application.run_polling()