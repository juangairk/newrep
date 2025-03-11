from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
import os
from  dotenv import  load_dotenv
load_dotenv()
# Токен вашего бота
TOKEN = os.getenv('key')

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Команда /start выполнена")
    await update.message.reply_text('Привет! Я ваш бот. Пока я ничего не умею, но скоро научусь!')

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Команда /help выполнена")
    await update.message.reply_text('Вот список доступных команд:\n'
        '/start - Начать работу с ботом\n'
        '/help - Получить справку\n'
        '/convert - Конвертировать валюту\n'
        '/weather - Узнать погоду')
# Обработчик команды /convert
async def convert_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Команда /convert выполнена")
    await update.message.reply_text('Функция конвертации валюты пока не реализована.')

# Обработчик команды /weather
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Команда /weather выполнена")
    await update.message.reply_text('Функция погоды пока не реализована. Скоро будет!')

async def goroskop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Команда /convert выполнена")
    await update.message.reply_text('Функция гороскоп пока не реализована.')

# Регистрация команд
async def set_commands(application):
    logger.info("Установка команд бота")
    await application.bot.set_my_commands([
        BotCommand("start", "Запустить бота"),
        BotCommand("help", "Получить справку"),
        BotCommand("convert", "Конвертировать валюту"),
        BotCommand("weather", "Прогноз погоды"),
        BotCommand("goroskop", "Функция гороскоп"),
    ])

# Основная функция
def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('convert', convert_command))
    application.add_handler(CommandHandler('weather', weather_command))
    application.add_handler(CommandHandler('goroskop', goroskop_command))
    # Регистрируем команды для отображения в интерфейсе

    application.run_polling()

if __name__ == '__main__':
    print("бот запущен...")
    main()