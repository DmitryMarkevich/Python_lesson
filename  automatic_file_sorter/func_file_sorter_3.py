import os
import shutil
from typing import Tuple


def read_directory(dir_: str) -> Tuple[str, str, str]:
    """
    The function takes in string format - the path to the directory.
    Returns a tuple of three elements: file name with extension, file name, file extension.

    """
    for file in os.listdir(dir_):
        file_name, extension = os.path.splitext(file)

        yield file, file_name, extension


def display_a_message(data: dict, file_name: str, key_: str, parameter=True) -> None:
    """
    The function takes a dictionary with data and a file name.
    Prints to the console information about moving files through directories.

    """
    print(f"Файл {file_name}"
          f" {'перемещен в папку' if parameter else 'уже есть в папке'} "
          f"{os.path.basename(data[key_])}")


def main():
    # Директория с файлами для сортировки
    directory = r"d:/directory_sort"

    # Целевые директории для перемещения файлов
    data_dictionary = {
        (".docx", ".pdf"): "d:/Sorting/documents",
        (".jpg", ".png"): "d:/Sorting/foto",
        (".mp3", ".mp4", ".wav"): "d:/Sorting/music",
        (".avi",): "d:/Sorting/video"
    }

    # Циклом for перебираем функцию-генератор read_directory
    for file, file_name, extensions in read_directory(directory):
        # Циклом for перебираем ключи словаря data_dictionary
        for file_extensions in data_dictionary:
            # Если расширение файла присутствует в ключе словаря
            if extensions.lower() in file_extensions:
                # Перемещаем файл в целевую директорию
                try:
                    shutil.move(src=rf"{directory}/{file}", dst=data_dictionary[file_extensions])
                    # Выводим в консоль сообщение какой файл в какую директорию переместили
                    display_a_message(data_dictionary, file_name, file_extensions)

                # Обработка исключения если такой файл в целевой директории уже есть
                except shutil.Error:
                    display_a_message(data_dictionary, file_name, file_extensions, parameter=False)

    print(f"\nОбработка директории '{os.path.basename(directory)}' завершена.")


# Вызов функци main
main()
