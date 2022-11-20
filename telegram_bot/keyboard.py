from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Основа для кнопок

info = types.KeyboardButton("/Информация")  # Кнопка информации
stats = types.KeyboardButton("/Статистика")  # Кнопка статистики

# Добавляем кнопки в основу бота
start.add(stats)
start.add(info)

if __name__ == '__main__':
    print("Этот файл нужно импортировать.")
