import subprocess
import time

from datetime import timedelta
import asyncio, os
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.types.input_file import FSInputFile
from aiogram.types.inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from aiogram.types.inline_query_result_article import InlineQueryResultArticle
from aiogram.types.input_text_message_content import InputTextMessageContent

import requests
from asgiref.sync import sync_to_async
import base64

from filter import MaxLenght, CommandPing

count = 0
requests.post = sync_to_async(requests.post)

init_ts = time.perf_counter()
name = ""

# First commit?

async def update_name():
    global name
    subprocess.run(["./env/Scripts/python", "userbot.py"])
    with open("name.txt", "r", encoding="utf-8") as file:
        name = file.read()


def uptime() -> int:
    return round(time.perf_counter() - init_ts)


class Filters:
    @staticmethod
    def lenght(text: str):
        return len(text) > 70


async def create_sticker(text: str, name):
    global count
    path = f"./photo/{count}.png"
    json = {
        "type": "quote",
        "format": "png",
        "backgroundColor": "#1b1429",
        "width": 4096,
        "height": 4096,
        "scale": 2,
        "messages": [
            {
                "entities": [],
                "chatId": 2050167589,
                "avatar": True,
                "from": {
                    "id": 2050167589,
                    "first_name": name,
                    "last_name": "",
                    "username": "alua_krr",
                    "language_code": "ru",
                    "title": name,
                    "emojiBrand": {
                          "_": "EmojiStatus",
                          "custom_emoji_id": 5458809708439677487
                      },
                    "photo": {
                        "small_file_id": "AQADAgADEdExG8GICEsAEAIAAyUTM3oABOHVNo6TChPyAAQeBA",
                        "small_photo_unique_id": "AgADEdExG8GICEs",
                        "big_file_id": "AQADAgADEdExG8GICEsAEAMAAyUTM3oABOHVNo6TChPyAAQeBA",
                        "big_photo_unique_id": "AgADEdExG8GICEs"
                    },
                    "type": "private",
                    "name": name
                },
                "text": text,
                "replyMessage": {}
            }
        ]
    }
    count += 1
    response = (await requests.post('https://bot.lyo.su/quote/generate', json=json)).json()
    buffer = base64.b64decode(response['result']['image'].encode('utf-8'))

    open(path, 'wb+').write(buffer)

    return path


logging.basicConfig(level=logging.INFO)

TOKEN_TEST = "5340042795:AAEHnRAutcZ_pCnaULca5dVcmPeE_itrspY"
TOKEN = "6779483668:AAHWvZzxjAG5qiFHYND9hlDtCJNVv9mT-y4"  # "6779483668:AAHWvZzxjAG5qiFHYND9hlDtCJNVv9mT-y4"
bot = Bot(token=TOKEN_TEST)

dp = Dispatcher()
router = Router()
dp.include_router(router)


@router.message(Command("ping"))
async def ping(message: types.Message):
    start = time.perf_counter_ns()
    message2 = await message.answer("🌒")

    await message2.edit_text(
        f"🏓 Ping: {round((time.perf_counter_ns() - start) / 10 ** 6, 3)} ms\n📡 Uptime: {str(timedelta(seconds=uptime()))}"
    )


@router.message(MaxLenght())
async def max_lenght(message: types.Message):
    await message.answer(
        "Максимальная длина текста 70 символов"
    )


@router.message(F.text)
async def answer_message(message: types.Message):
    if Filters.lenght(message.text):
        await message.answer(
            "Максимальная длина текста 70 символов"
        )
        return

    path = await create_sticker(message.text, name)
    await message.answer_sticker(FSInputFile(path))
    os.remove(path)


@router.inline_query(CommandPing())
async def ping_inline(inline_query: types.InlineQuery, bot: Bot):
    start = time.perf_counter_ns()
    message = await bot.send_message(2028784660, "🌒")
    text = f"🏓 Ping: {round((time.perf_counter_ns() - start) / 10 ** 6, 3)} ms\n📡 Uptime: {str(timedelta(seconds=uptime()))}"
    await message.delete()
    results = [InlineQueryResultArticle(
        id="1",
        title="🏓 Ping",
        description=text,
        input_message_content=InputTextMessageContent(
            message_text=text
        )
    )]
    await inline_query.answer(results, is_personal=True)


@router.inline_query()
async def answer_inline(inline_query: types.InlineQuery):
    if Filters.lenght(inline_query.query):
        await inline_query.answer([], is_personal=True,
                                  switch_pm_parameter="max_lenght",
                                  switch_pm_text="Текст должен быть размером <70 символов")
        return

    results = []
    path = await create_sticker(inline_query.query, name)
    sticker = await bot.send_sticker(2028784660, FSInputFile(path))
    os.remove(path)

    results.append(
        InlineQueryResultCachedSticker(
            type='sticker',
            id='1',
            sticker_file_id=sticker.sticker.file_id,
            reply_markup=None,
            input_message_content=None
        )
    )
    await sticker.delete()
    await inline_query.answer(results, is_personal=True)


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_name, 'interval', minutes=30)
    scheduler.start()

    await update_name()

    await dp.start_polling(bot)


asyncio.run(main())
