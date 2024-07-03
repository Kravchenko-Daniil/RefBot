import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, callback_data
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import API


# Bot token can be obtained via https://t.me/BotFather
TOKEN = API

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
сallback = callback_data.CallbackData('pre', 'action', 'floor')

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.callback_query()
async def ref_generate_spa(message: Message) -> str:
    await message.answer('Ты выбрал спа')


@dp.message()
async def echo_handler(message: Message) -> None:
    # """
    # Handler will forward receive a message back to the sender
    #
    # By default, message handler will handle all message types (like a text, photo, sticker etc.)
    # """
    # try:
    #     # Send a copy of the received message
    #     await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
    #     # But not all the types is supported to be copied so need to handle it
    #     await message.answer("Nice try!")

    buttons = [
        [InlineKeyboardButton(text="Спа", callback_data=сallback.new(action='1', floor=2))],
        [InlineKeyboardButton(text="Рефшара", callback_data=сallback.new(action='2', floor=2))]
    ]

    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer('Выбери вариант', reply_markup=markup)


@dp.callback_query_handler(сallback.filter())
async def button_press(call: CallbackQuery, callback_data: dict):
    action = callback_data.get('action')  # 1 or 2
    floor = callback_data.get('floor')  # 2

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())