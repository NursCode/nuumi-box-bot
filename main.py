from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
import logging

# 🔐 Токен твоего нового бота
API_TOKEN = '7916131360:AAFHEmw5SZnxlR8mLSyhIfIFxyYU60ttddA'

# Включаем логгирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопка для запуска Mini App
webapp_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="🎁 Открыть Сюрприз от NUUMI",
        web_app=WebAppInfo(url="https://nuumi-miniapp.onrender.com")
    )]
])

# Обработка /start
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.answer(
        "Солнце моё ☀️\nГотова коробочка с сюрпризом от NUUMI — открой прямо сейчас!",
        reply_markup=webapp_keyboard
    )

# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
