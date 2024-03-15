from aiogram.filters import BaseFilter
from aiogram.types import Message, InlineQuery


class MaxLenght(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        arg = message.text[7:]
        return arg == "max_lenght"


class CommandPing(BaseFilter):
    async def __call__(self, inline_query: InlineQuery) -> bool:
        arg = inline_query.query
        return arg == "ping"


class Filters:
    @staticmethod
    def lenght(text: str):
        return len(text) > 70
