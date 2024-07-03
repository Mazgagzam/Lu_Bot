import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers.handler import router

logger = logging.getLogger(__name__)

TOKEN = "012345678:ABC"

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    bot = Bot(token=TOKEN)

    dp = Dispatcher(bot)

    dp.include_router(router)

  
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

def cli():
    """Wrapper for command line"""
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

if __name__ == '__main__':
    cli()
