import asyncio
from aiogram import Bot,Dispatcher

import os
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()
mytoken = os.getenv('key2')


async  def main():
    bot = Bot(token=mytoken)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print("bot starting...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot ending")