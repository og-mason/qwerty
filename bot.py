import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

WEBAPP_URL = "https://og-mason.github.io/qwerty/" 

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="▶️ Играть", web_app=WebAppInfo(url=WEBAPP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer(
    "Привет 👋 Добро пожаловать в игру 🎮 'Угадай число'!\n\n"
    "Правила простые:\n"
    "🎯 Точное попадание: +3 очка\n"
    "👍 Почти угадал (±5): +1 очко\n"
    "❌ Промах: -1 очко\n\n"
    "Каждое очко = 1 звезда ⭐ в Telegram!\n\n"
    "Жми кнопку ниже, чтобы начать играть и зарабатывать 👇",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
