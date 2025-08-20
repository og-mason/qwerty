# import asyncio
# import logging
# import random
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from config import BOT_TOKEN
# from storage import ScoreStorage
# from game_logic import NumberGuessGame

# logging.basicConfig(level=logging.INFO)

# # Инициализация
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# # Хранилище
# storage = ScoreStorage()
# games = {}  # user_id -> NumberGuessGame


# @dp.message(Command("start"))
# async def start_game(message: types.Message):
#     user_id = str(message.from_user.id)
#     games[user_id] = NumberGuessGame(user_id, storage)
#     await message.answer(
#         "🎮 Добро пожаловать в игру 'Угадай число'!\n\n"
#         "Правила:\n"
#         " - 🎯 Точное попадание = +3 очка\n"
#         " - ±5 от числа = +1 очко\n"
#         " - иначе -1 очко\n\n"
#         "Введи число от 1 до 100 👇"
#     )

# @dp.message()
# async def handle_guess(message: types.Message):
#     user_id = str(message.from_user.id)

#     if user_id not in games:
#         games[user_id] = NumberGuessGame(user_id, storage)

#     try:
#         number = int(message.text)
#     except ValueError:
#         await message.answer("⚠️ Введи число от 1 до 100!")
#         return

#     game = games[user_id]
#     result = game.guess(number)
#     await message.answer(result)

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

WEBAPP_URL = "https://yourdomain.com/game"  # здесь будет твой URL (где лежит webapp)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="▶️ Играть", web_app=WebAppInfo(url=WEBAPP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Привет 👋 Это игра 🎮 'Угадай число'!\n"
        "Жми кнопку ниже, чтобы открыть игру 👇",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
