import os
import time
from datetime import timedelta

from aiogram import Bot, types, Router, F
from aiogram.filters import Command
from aiogram.types.input_file import FSInputFile
from aiogram.types.inline_query_result_cached_sticker import InlineQueryResultCachedSticker
from aiogram.types.inline_query_result_article import InlineQueryResultArticle
from aiogram.types.input_text_message_content import InputTextMessageContent

from middleware import Middleware
from get_name import name
from create_sticker import create_sticker
from filter import MaxLenght, InlineCommand, Filters

router = Router()
router.inline_query.middleware(Middleware())
router.message.middleware(Middleware())

init_ts = time.perf_counter()


def uptime() -> int:
    return round(time.perf_counter() - init_ts)


@router.message(Command("ping"))
async def ping(message: types.Message):
    start = time.perf_counter_ns()
    message2 = await message.answer("🌒")

    await message2.edit_text(
        f"🏓 Ping: {round((time.perf_counter_ns() - start) / 10 ** 6, 3)} ms\n📡 Uptime: {str(timedelta(seconds=uptime()))}"
    )


@router.message(Command("stat"))
async def stat(message: types.Message, statistics):
    await message.answer(
        statistics.get_data()
    )


@router.message(MaxLenght())
async def max_lenght(message: types.Message):
    await message.answer(
        "Максимальная длина текста 70 символов"
    )


@router.message(F.text)
async def answer_message(message: types.Message, statistics):
    if Filters.lenght(message.text):
        await message.answer(
            "Максимальная длина текста 70 символов"
        )
        return

    path = await create_sticker(message.text, name, statistics.count)
    await message.answer_sticker(FSInputFile(path))
    statistics += 1
    os.remove(path)


@router.inline_query(InlineCommand("stat"))
async def stat_inline(inline_query: types.InlineQuery, statistics):
    text = statistics.get_data()
    results = [InlineQueryResultArticle(
        id="1",
        title="📊 Статистика",
        description=text,
        input_message_content=InputTextMessageContent(
            message_text=text
        )
    )]
    await inline_query.answer(results, is_personal=True)


@router.inline_query(InlineCommand("ping"))
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
async def answer_inline(inline_query: types.InlineQuery, bot: Bot, statistics):
    if Filters.lenght(inline_query.query):
        await inline_query.answer([], is_personal=True,
                                  switch_pm_parameter="max_lenght",
                                  switch_pm_text="Текст должен быть размером <70 символов")
        return

    results = []
    path = await create_sticker(inline_query.query, name, statistics.count)
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
    statistics += 1
