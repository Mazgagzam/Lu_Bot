from aiogram.filters import BaseFilter
from aiogram.types import Message, InlineQuery


class MaxLenght(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not isinstance(message, Message):
            return False

        arg = message.text[7:]
        return arg == "max_lenght"


class InlineCommand(BaseFilter):
    def __init__(self, arg: str = ""):
        self.arg = arg

    async def __call__(self, inline_query: InlineQuery) -> bool:
        arg = inline_query.query
        return arg == self.arg


class Filters:
    @staticmethod
    def lenght(text: str):
        return len(text) > 70
