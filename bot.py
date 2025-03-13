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
if name == "main":  # ВАЖНО! Два подчеркивания с обеих сторон!
    print("Бот запущен...")
    application.run_polling()
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os

# Токен бота
TOKEN = "7416695404:AAE18OU0B0BfJf3E8wAFpHo9psJ8TgwBZbg"

# Список админов (вставь свой Telegram ID)
ADMINS = {6739219512}  # ЗАМЕНИ на свой Telegram ID!

# Список пользователей (храним в памяти)
users = set()

# Функция проверки, является ли пользователь админом
def is_admin(user_id):
    return user_id in ADMINS

# Команда /start
async def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id in users or is_admin(user_id):
        await update.message.reply_text("Привет! Ты можешь пользоваться ботом.")
    else:
        await update.message.reply_text("⛔ Доступ запрещен. Обратись к администратору.")

# Команда /add_user (Только для админов)
async def add_user(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not is_admin(user_id):
        await update.message.reply_text("⛔ У тебя нет прав на добавление пользователей.")
        return
    
    if not context.args:
        await update.message.reply_text("⚠ Используй: /add_user @username")
        return
    
    username = context.args[0].replace("@", "")
    users.add(username)
    await update.message.reply_text(f"✅ Пользователь @{username} добавлен!")

# Команда /list_users (Показать список пользователей)
async def list_users(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not is_admin(user_id):
        await update.message.reply_text("⛔ У тебя нет прав.")
        return

    if not users:
        await update.message.reply_text("📋 Список пользователей пуст.")
    else:
        user_list = "\n".join([f"@{user}" for user in users])
        await update.message.reply_text(f"📋 Список пользователей:\n{user_list}")

# Команда /remove_user (Удалить пользователя)
async def remove_user(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not is_admin(user_id):
        await update.message.reply_text("⛔ У тебя нет прав на удаление пользователей.")
        return
    
    if not context.args:
        await update.message.reply_text("⚠ Используй: /remove_user @username")
        return
    
    username = context.args[0].replace("@", "")
    if username in users:
        users.remove(username)
        await update.message.reply_text(f"✅ Пользователь @{username} удален!")
    else:
        await update.message.reply_text(f"⚠ Пользователь @{username} не найден.")

# Создаем приложение
application = Application.builder().token(TOKEN).build()

# Добавляем обработчики команд
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("add_user", add_user))
application.add_handler(CommandHandler("list_users", list_users))
application.add_handler(CommandHandler("remove_user", remove_user))

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    application.run_polling()