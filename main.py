from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio

from config import API


dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.start_polling()

asyncio.run(main())