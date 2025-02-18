import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.token import TokenValidationError
import os

TOKEN = '8084801256:AAG4TOESGCV-4v1f6LH7k4V2tmR9jU5EAm8'  # Используй переменные окружения для безопасности
CHANNEL_LINK = "https://t.me/qwe1ewqbot"  # Замени на свою ссылку

# Проверяем токен перед запуском
try:
    bot = Bot(token=TOKEN)
except TokenValidationError:
    print("Ошибка: Некорректный токен. Проверьте BOT_TOKEN.")
    exit(1)

dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Я человек", callback_data="human")],
        [InlineKeyboardButton(text="❌ Я бот", callback_data="bot")]
    ])
    await message.answer("Подтвердите, что вы человек, нажав на ✅", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data in ["human", "bot"])
async def captcha_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "human":
        await callback_query.message.answer(f"Вы подтверждены! Вот ссылка на канал: {CHANNEL_LINK}")
    else:
        await callback_query.message.answer("Ошибка! Попробуйте снова.")
    await callback_query.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())