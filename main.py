import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers.handler import router

logging.basicConfig(level=logging.INFO)

TOKEN_TEST = "5340042795:AAEHnRAutcZ_pCnaULca5dVcmPeE_itrspY"
TOKEN = "6779483668:AAHWvZzxjAG5qiFHYND9hlDtCJNVv9mT-y4"


async def main():
    bot = Bot(token=TOKEN_TEST)

    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())