import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile

BOT_TOKEN = "8605851489:AAGFXGDVNAknWiIg_NP0ZGT3JtfHOM9sdrA"
IMAGE_PATH = "1000039092.jpg"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

counters = {}

@dp.message()
async def handle(message: Message):
    if message.chat.type not in ["group", "supergroup"]:
        return
    
    chat_id = message.chat.id
    counters[chat_id] = counters.get(chat_id, 0) + 1
    
    if counters[chat_id] % 20 == 0:
        try:
            await message.answer_photo(FSInputFile(IMAGE_PATH))
        except:
            pass

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())