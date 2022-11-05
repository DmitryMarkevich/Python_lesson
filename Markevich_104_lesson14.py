from typing import Union


def write_to_file(file_: str, array: Union[list, tuple]) -> None:
    """
    The function accepts a target file and an array with data to write to the file.

    """
    try:
        with open(file_, 'w', encoding='utf-8') as file:
            for element in array:
                if isinstance(element, int):
                    element = str(element)
                file.write(element + '\n')
    except FileNotFoundError:
        print("Невозможно открыть файл.")


def read_file_1(file_: str) -> list:
    """
    The function accepts a target file for reading data.
    Returns a list with numbers in ascending order, followed by strings in ascending order of their length.
    """
    try:
        with open(file_, 'r', encoding='utf-8') as file:
            data = {'numbers': [], 'letters': []}
            for line in file:
                line = line.strip()
                if line.isdigit():
                    data['numbers'].append(int(line))
                else:
                    data['letters'].append(line)

            return sorted(data['numbers']) + sorted(data['letters'], key=len)

    except FileNotFoundError:
        print("Невозможно открыть файл.")


def read_file_2(file_: str) -> list:
    """
    The function accepts a target file for reading data.
    Returns a list with numbers in ascending order, followed by strings in ascending order of their length.

    """
    try:
        with open(file_, 'r', encoding='utf-8') as file:
            list_numbers = sorted([int(i) for i in file if i.strip().isdigit()])
            file.seek(0)
            list_letters = sorted([i.strip() for i in file if i.strip().isalpha()], key=len)

            return list_numbers + list_letters

    except FileNotFoundError:
        print("Невозможно открыть файл.")


def element_conversion(x: Union[int, str]) -> int:
    """
    The function accepts a number or a string.
    If a number arrives, it returns the same number.
    If the function takes a string, it returns the length of that string plus 1000.

    """
    if isinstance(x, int):
        return x
    return len(x) + 1000


def read_file_3(file_: str) -> list:
    """
    The function accepts a target file for reading data.
    Returns a list with numbers in ascending order, followed by strings in ascending order of their length.

    """
    try:
        with open(file_, 'r', encoding='utf-8') as file:
            d_list = file.readlines()
            list_numbers = sorted([int(i) for i in d_list if i.strip().isdigit()])
            list_letters = sorted([i.strip() for i in d_list if i.strip().isalpha()], key=len)

            return list_numbers + list_letters

    except FileNotFoundError:
        print("Невозможно открыть файл.")


def read_file_4(file_: str) -> list:
    """
    The function accepts a target file for reading data.
    Returns a list with numbers in ascending order, followed by strings in ascending order of their length.

    """
    try:
        with open(file_, 'r', encoding='utf-8') as file:
            d_list = file.readlines()

            return sorted([int(i) if i.strip().isdigit() else i.strip() for i in d_list], key=element_conversion)

    except FileNotFoundError:
        print("Невозможно открыть файл.")


def read_file_5(file_: str) -> list:
    """
    The function accepts a target file for reading data.
    Returns a list with numbers in ascending order, followed by strings in ascending order of their length.

    """
    try:
        with open(file_, 'r', encoding='utf-8') as file:
            return sorted([int(i) if i[:-1].isdigit() else i[:-1] for i in file.readlines()], key=element_conversion)

    except FileNotFoundError:
        print("Невозможно открыть файл.")


def sort_array(array: Union[list, tuple]) -> list:
    """
    The function takes an array of numbers and strings.
    Returns a sorted array: at the beginning of the string in ascending order of their length,
    and then the digits in ascending order.

    """
    string_array = [i for i in array if isinstance(i, str)]
    array_of_numbers = [i for i in array if isinstance(i, int)]

    return sorted(string_array, key=len) + sorted(array_of_numbers)


data_list = [100, 'python', 50, 'hello', 25, 'file', 500, 'lesson17_OOP']
f = "file_lesson_14.txt"

# Запись в файл
# write_to_file(f, data_list)

# Несколько функций для чтения из файла
# print(read_file_1(f))
# print(read_file_2(f))
# print(read_file_3(f))
# print(read_file_4(f))
# print(read_file_5(f))

# Запись в файл с применением функции для сортировки
write_to_file(f, sort_array(data_list))
