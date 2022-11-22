from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Основа для кнопок

info = types.KeyboardButton("Информация")  # Кнопка информации
stats = types.KeyboardButton("Статистика")  # Кнопка статистики
razrab = types.KeyboardButton("Разработчик")  # Кнопка разработчика
registration = types.KeyboardButton("Регистрация")  # Кнопка разработчика

# Добавляем кнопки в основу бота
start.add(stats, info)
start.add(razrab, registration)

"""______________________________________________________________________________________________________________"""

stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton(f'Да', callback_data='join'))
stats.add(InlineKeyboardButton(f'Нет', callback_data='cancel'))


if __name__ == '__main__':
    print("Этот файл нужно импортировать.")
