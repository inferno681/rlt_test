import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from json import dumps

from config_reader import config
from db import aggregate
from validation import input_check

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN.get_secret_value())

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hi {message.from_user.first_name}!")


@dp.message()
async def data_aggregation(message: types.Message):
    check_message = input_check(message.text)
    if not check_message[0]:
        await message.answer(check_message[1])
    else:
        result = await aggregate(check_message[1])
        await message.answer(
            dumps({
                "dataset": list(result.values()),
                "labels": list(result.keys())
            })
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
