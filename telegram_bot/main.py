from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config  # Импортируем файл config
from keyboard import start  # Импортируем файл keyboard

import logging

storage = MemoryStorage()  # FSM
#  Инициализируем бота
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
#  Инициализируем диспетчер к нашему боту
dp = Dispatcher(bot, storage=storage)  # хранилище состояний в оперативной памяти
#  Включаем логирование
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    filename='log.txt', level=logging.INFO)

count = 0


@dp.message_handler(commands="start")
#  Задаем функцию, которая отправит сообщение на команду "start"
async def welcome(message: types.Message):
    with open("user.txt", "r") as joined_file:
        joined_users = set()
        for line in joined_file:
            joined_users.add(line.strip())

    if not str(message.chat.id) in joined_users:
        with open("user.txt", "a") as joined_file:
            joined_file.write(str(message.chat.id) + '\n')
            joined_users.add(message.chat.id)

    await bot.send_message(message.chat.id, f"ПРИВЕТ, *{message.from_user.first_name},* БОТ РАБОТАЕТ",
                           reply_markup=start, parse_mode='Markdown')


@dp.message_handler(commands="Информация")
#  Задаем функцию, которая отправит сообщение на команду "Информация"
async def cmd_test2(message: types.Message):
    global count
    str_info = ''
    try:
        with open('info.txt', 'r', encoding='utf-8') as file:
            for line in file:
                str_info += line

    except FileNotFoundError:
        print("Невозможно открыть файл.")
    count += 1
    await message.reply(str_info)


@dp.message_handler(commands="Статистика")
#  Задаем функцию, которая отправит сообщение на команду "Статистика"
async def cmd_test3(message: types.Message):
    await message.reply(f"Количество запросов по литературе: {count}")


#  Создаем точку входа
if __name__ == "__main__":
    print("The bot is running.")  # Сообщаем, что бот запущен
    #  Запускаем бота в режиме start_polling (бот будет постоянно получать и отвечать на сообщения)
    executor.start_polling(dp, skip_updates=True)
