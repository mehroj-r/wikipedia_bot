import asyncio
import logging
import sys
import wikipedia

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Defining Wikipedia Language
wikipedia.set_lang("en")

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6583942031:AAFg210_atreTpKav8wRxRE84kt3ReKWVsE"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


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
    await message.reply(f"Hello, {hbold(message.from_user.full_name)}! \nWelcome to Wikipedia Bot. Send any text message to get information about.")


@dp.message()
async def wiki_handler(message: types.Message) -> None:
    try:
        wiki_response = wikipedia.summary(message.text)
        # Send a copy of the received message
        await message.answer(wiki_response)     
    except:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("No wikipedia page was found for this request !!!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())