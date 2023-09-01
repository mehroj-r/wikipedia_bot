import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from wiki_api import wiki_response

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "BOT_TOKEN"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.reply(f"Hello, {hbold(message.from_user.full_name)}! \nWelcome to Wikipedia Bot. Send any text message to get information about.")


@dp.message()
async def wiki_handler(message: types.Message) -> None:
    try:
        # Send a response from Wikipedia API
        response = wiki_response(message.text)
        await message.answer(response)
    except:
        # But not all the inputs are supported
        await message.answer("No wikipedia page was found for this request !!!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())