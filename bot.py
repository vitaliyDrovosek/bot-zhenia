import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

# ========== ТОКЕН ВТОРОГО БОТА ==========
BOT_TOKEN = "8605851489:AAGFXGDVNAknWiIg_NP0ZGT3JtfHOM9sdrA"

# ПУТЬ К ТВОЕЙ КАРТИНКЕ
IMAGE_PATH = "1000039092.jpg"  # Картинка в той же папке

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

message_counter = 0

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Бот работает")

@dp.message()
async def handle_message(message: Message):
    global message_counter
    
    message_counter += 1
    
    if message_counter % 20 == 0:
        try:
            photo = FSInputFile(IMAGE_PATH)
            await message.answer_photo(photo)
        except Exception as e:
            print(f"Ошибка: {e}")

async def main():
    print("Бот с картинкой запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())