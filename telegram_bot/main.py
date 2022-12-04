from aiogram import Bot, types
from aiogram.types import ContentType, Message
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

from Lesson.telegram_bot import config
import keyboard  # Импортируем файл keyboard

import logging
from random import choice

storage = MemoryStorage()  # FSM
#  Инициализируем бота
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
#  Инициализируем диспетчер к нашему боту
dp = Dispatcher(bot, storage=storage)  # хранилище состояний в оперативной памяти
#  Включаем логирование
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    filename='log.txt', level=logging.INFO)

"""_______________________________________________FSM________________________________________________________"""


class Meinfo(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(Command("me"), state=None)  # Создаем команду /me для админа
async def enter_meinfo(message: types.Message):
    if message.chat.id == config.admin:
        await message.answer("Начинаем настройку.\n"
                             "№1 Введите линк на ваш профиль.")  # Бот спрашивает ссылку

        await Meinfo.Q1.set()  # И начинает ждать наш ответ


@dp.message_handler(state=Meinfo.Q1)  # Как только бот получит ответ, вот это выполнится
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)  # Тут же он записывает наш ответ (наш линк)

    await message.answer("Линк сохранен. \n"
                         "№2 Введите текст.")

    await Meinfo.Q2.set()  # Ждет пока мы введем текст


@dp.message_handler(state=Meinfo.Q2)  # Текст пришел а значит переходим к этому шагу
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)  # Записываем второй ответ

    await message.answer("Текст сохранен.")

    data = await state.get_data()
    answer1 = data.get("answer1")  # Здесь берутся ответы из словаря и присваиваются переменным
    answer2 = data.get("answer2")

    with open("link.txt", 'w', encoding='utf-8') as joinedFile:
        joinedFile.write(str(answer1))

    with open("text.txt", 'w', encoding='utf-8') as joinedFile:
        joinedFile.write(str(answer2))

    await message.answer(f"Ваша ссылка на профиль: {answer1}\nВаш текст:\n{answer2}")

    await state.finish()


"""_______________________________________________FSM_registration____________________________________________"""

# class MeinfoReg(StatesGroup):
#     Q1 = State()
#     Q2 = State()
#     Q3 = State()
#
#
# @dp.message_handler(text_contains='Регистрация', state=None)  # Отлавливаем соообщение "Регистрация"
# async def enter_meinfo_new(message):
#     if message.chat.id:
#         await message.answer("Начинаем регистрацию.\n"
#                              "№1 Введите Ваше имя.")  # Бот спрашивает имя
#
#         await MeinfoReg.Q1.set()  # И начинает ждать наш ответ
#
#
# @dp.message_handler(state=MeinfoReg.Q1)  # Как только бот получит ответ, вот это выполнится
# async def answer_q1(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(answer1=answer)  # Тут же он записывает наш ответ
#
#     await message.answer("Имя записано. \n"
#                          "№2 Введите фамилию.")
#
#     await MeinfoReg.Q2.set()  # Ждет пока мы введем текст
#
#
# @dp.message_handler(state=MeinfoReg.Q2)  # Текст пришел а значит переходим к этому шагу
# async def answer_q2(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(answer2=answer)  # Записываем второй ответ
#
#     await message.answer("Фамилия записана.\n"
#                          "№3 Введите телефон.")
#
#     await MeinfoReg.Q3.set()  # Ждет пока мы введем текст
#
#
# @dp.message_handler(state=MeinfoReg.Q3)  # Текст пришел а значит переходим к этому шагу
# async def answer_q3(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(answer3=answer)  # Записываем второй ответ
#
#     await message.answer("Данные приняты.")
#
#     data = await state.get_data()
#     answer1 = data.get("answer1")  # Здесь берутся ответы из словаря и присваиваются переменным
#     answer2 = data.get("answer2")
#     answer3 = data.get("answer3")
#
#     with open("user_data.txt", 'a', encoding='utf-8') as joinedFile:
#         joinedFile.write(str(answer1 + ',' + answer2 + ',' + answer3 + '\n'))
#
#     await message.answer("Регистрация прошла успешно.")
#
#     await state.finish()


"""_______________________________________________start______________________________________________________"""


@dp.message_handler(commands="start", commands_prefix='!/', state=None)
#  Задаем функцию, которая отправит сообщение на команду "start"
async def welcome(message):
    with open("user.txt", "r") as joinedFile:
        joinedUsers = set()
        for line in joinedFile:
            joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        with open("user.txt", "a") as joinedFile:
            joinedFile.write(str(message.chat.id) + '\n')
            joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f"ПРИВЕТ, *{message.from_user.first_name},* БОТ РАБОТАЕТ",
                           reply_markup=keyboard.start, parse_mode='Markdown')


"""_______________________________________________/rassilka_____________________________________________________"""


@dp.message_handler(commands=['rassilka'], commands_prefix='!/')
# задаем функцию обработчик
async def mailing_list(message: types.Message):
    # сверяем id пославшего сообщение с id админа
    if message.chat.id == config.admin:
        # отправляем сообщение
        await bot.send_message(message.chat.id, f'Рассылка началась'
                                                f'\nБот оповестит, когда закончит рассылку',
                               parse_mode=types.ParseMode.MARKDOWN_V2)
        # задаем переменные для хранения принявших и заблокировавших
        recieve_users, block_users = 0, 0
        # открываем fm_user.txt в режиме чтения
        with open('user.txt', 'r') as file:
            # создаем множество всех пользователей
            joinedUsers = set()
            # проходим циклу по всем id в файле
            for line in file:
                # добавляем во множество id
                joinedUsers.add(line.strip())
            # запускаем цикл
            for user in joinedUsers:
                try:
                    await bot.send_photo(user, open('photo.PNG', 'rb'), (message.text[message.text.find(' '):]
                                                                         if ' ' in message.text else "Вот Вам фото"))
                    recieve_users += 1
                except:
                    block_users += 1
                await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, f'Рассылка завершена \n'
                                                    f'Сообщение получили: {recieve_users} пользователей \n'
                                                    f'Заблокировали бота: {block_users}',
                                   parse_mode=types.ParseMode.MARKDOWN_V2)


"""_________________________________________Отправить фото_____________________________________________________"""


@dp.message_handler(text_contains='Отправить фото', state=None)
# задаем функцию обработчик
async def to_send_a_photo(message: types.Message):
    if message.chat.id:
        # отправляем сообщение
        await bot.send_message(message.chat.id, f'Вот фото'
                                                f'\nдля Вас:',
                               parse_mode=types.ParseMode.MARKDOWN_V2)
        # задаем переменные для хранения принявших и заблокировавших
        recieve_users, block_users = 0, 0
        # открываем fm_user.txt в режиме чтения
        with open('user.txt', 'r') as file:
            # создаем множество всех пользователей
            joinedUsers = set()
            # проходим циклу по всем id в файле
            for line in file:
                # добавляем во множество id
                joinedUsers.add(line.strip())
            # запускаем цикл
            for user in joinedUsers:
                if user == str(message.chat.id):
                    foto = choice(['img.png', 'img_1.png', 'img_2.png', 'img_3.png', 'img_4.png', 'photo.PNG'])
                    try:
                        await bot.send_photo(user, open(foto, 'rb'))
                        recieve_users += 1
                    except:
                        block_users += 1
                    await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, 'Жми снова, если хочешь еще получить фото.')


"""____________________________'photo'___Бот возвращает id фото, которое мы ему передали________________________"""

# @dp.message_handler(content_types=ContentType.PHOTO)  # Бот возвращает id фото, которое мы ему передали
# async def get_photo(message: Message):
#     await message.reply(message.photo[-1].file_id)


"""____________________________'photo'___Бот сохраняет фото, которое мы ему передали____________________________"""


@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    try:
        # chat_id = message.chat.id
        # file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        # downloaded_file = bot.download_file(file_path=file_info)
        print(message)

        file_info = message.photo[-1]['file_id']
        downloaded_file = bot.download_file(file_info)
        print(type(downloaded_file))

        src = r'C:\Users\Snegana\PycharmProjects\pythonProject\Lesson\telegram_bot\Photo\immmg.png'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        await message.reply(message, "Пожалуй, я сохраню это.")
    except Exception as e:
        await bot.send_message(message.chat.id, e)
    # chat_id = message.chat.id
    #
    # file_info = bot.get_file(message.document.file_id)
    # downloaded_file = bot.download_file(file_info.file_path)
    #
    # src = 'C:/Python/Project/tg_bot/files/received/' + message.document.file_name;
    # with open(src, 'wb') as new_file:
    #     new_file.write(downloaded_file)
    #
    # await bot.reply_to(message, "Пожалуй, я сохраню это")
    "____________________"
    # file_id = message.photo[-1].file_id
    # file_info = bot.get_file(file_id)
    # downloaded_file = bot.download_file(file_path=file_info)
    # with open("Photo/image.png", 'wb') as new_file:
    #     new_file.write(downloaded_file)


"""___________________________________________________join______________________________________________________"""


@dp.callback_query_handler(text_contains='join')
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt', 'r'))
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text=f'Вот статистика бота: *{d}* человек',
                                    parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text="У тебя нет админки\n Куда ты полез",
                                    parse_mode='Markdown')


"""________________________________________________cancel________________________________________________________"""


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Ты вернулся в главное меню. Жми опять кнопки ",
                                parse_mode='Markdown')


"""___________________________________________________ID________________________________________________________"""


@dp.callback_query_handler(text_contains='id')
async def my_id(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=f'Вот Ваш ID: *{call.message.chat.id}*',
                                parse_mode='Markdown')


"""________________________________________________back________________________________________________________"""


@dp.callback_query_handler(text_contains='back')
async def back(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text="Вы вернулись в главное меню.",
                                parse_mode='Markdown')


"""_______________________________________________________________________________________________________________"""


@dp.message_handler(content_types=['text'])
#  Задаем функцию, которая отправит сообщение на команды-сообщения "Статистика", "Информация" и "Разработчик"
async def get_message(message):
    if message.text == "Информация":
        await bot.send_message(message.chat.id, text="Информация \n Бот создан специально для обучения",
                               parse_mode='Markdown')

    if message.text == "Статистика":
        await bot.send_message(message.chat.id, text="Хочешь просмотреть статистику бота", reply_markup=keyboard.stats,
                               parse_mode='Markdown')

    if message.text == "Покажи пользователя":
        await bot.send_message(message.chat.id, text="Хочешь просмотреть свой ID?", reply_markup=keyboard.stats_1,
                               parse_mode='Markdown')

    if message.text == "Разработчик":
        with open("link.txt", 'r', encoding='utf-8') as link_1:
            link = link_1.read()

        with open("text.txt", 'r', encoding='utf-8') as text_1:
            text = text_1.read()

        await bot.send_message(message.chat.id, text=f"Создатель {link}\n{text}", parse_mode='HTML')


"""_____________________________________точка входа_____________________________________________________________"""

#  Создаем точку входа
if __name__ == "__main__":
    print("The bot is running.")  # Сообщаем, что бот запущен
    #  Запускаем бота в режиме start_polling (бот будет постоянно получать и отвечать на сообщения)
    executor.start_polling(dp, skip_updates=True)
