import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
import random
from keyboards import kb1, kb2
from randomFox import fox
from random import randint

API_TOKEN = config.token

#Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

#Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет,{name}! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.',reply_markup=kb1)

@dp.message(Command("stop"))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}!')

@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}!')
    await message.answer_photo(photo=img_fox)
    #await bot.send_photo(message.from_user.id, img_fox)

@dp.message(F.text.lower() == 'number')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f'{number}')

#Хэндлер
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет: {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я бот')
    elif 'кубик' in msg_user:
        await message.answer_dice(emote_id=random.randint(1, 100))
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри, что у меня есть, {name}!', reply_markup=kb2)
    else:
        await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())