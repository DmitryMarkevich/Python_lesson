from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Основа для кнопок

info = types.KeyboardButton("Информация")  # Кнопка информации
stats = types.KeyboardButton("Статистика")  # Кнопка статистики
razrab = types.KeyboardButton("Разработчик")  # Кнопка разработчика
# registration = types.KeyboardButton("Регистрация")  # Кнопка регистрация
registration = types.KeyboardButton("Покажи пользователя")  # Покажи пользователя
foto = types.KeyboardButton("Отправить фото")  # Покажи пользователя

# Добавляем кнопки в основу бота
start.add(stats, info)
start.add(razrab, registration)
start.add(foto)

"""______________________________________________________________________________________________________________"""

stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton(f'Да', callback_data='join'))
stats.add(InlineKeyboardButton(f'Нет', callback_data='cancel'))

stats_1 = InlineKeyboardMarkup()
stats_1.add(InlineKeyboardButton(f'Показать ID', callback_data='id'))
stats_1.add(InlineKeyboardButton(f'Вернутся назад', callback_data='back'))

if __name__ == '__main__':
    print("Этот файл нужно импортировать.")
