from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import os
from dotenv import load_dotenv

# Токен вашего бота
load_dotenv()
mytoken = os.getenv('key')

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Используй /convert <сумма> <валюта> для конвертации.')

# Обработчик команды /convert
async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount, currency = context.args
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        rate = data['rates'][currency.upper()]
        result = float(amount) * rate
        await update.message.reply_text(f'{amount} USD = {result} {currency.upper()}')
    except:
        await update.message.reply_text('Используй формат: /convert 100 EUR')

# Основная функция
def main():
    # Создаем приложение
    application = Application.builder().token(mytoken).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('convert', convert))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()