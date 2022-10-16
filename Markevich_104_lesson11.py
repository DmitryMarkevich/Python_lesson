from typing import List, Tuple, Union


def number_conversion(n: int) -> int:
    """
    The function takes the number n as input.
    Returns a number: n + nn + nnn.

    """
    return n + int(str(n) * 2) + int(str(n) * 3)


def even_and_odd_letters(str_: str) -> List[int]:
    """
    The function takes a string.
    Returns a list with the number of vowels and consonants.

    """
    dict_ = {"euioay": 0,
             "qwrtpsdfghjklzxcvbnm": 0
             }
    for i in str_.lower():
        for j in dict_:
            if i in j:
                dict_[j] += 1

    return list(dict_.values())


def return_value_from_x(x: int) -> int:
    """
    The function takes a number.
    Returns function values based on conditions:
    y = x ** 2 by -5 <= x <= 5
    y = 2 * |x| - 1 by x < -5
    y = 2x by x > 5

    """
    return x ** 2 if -5 <= x <= 5 else 2 * abs(x) - 1 if x < -5 else 2 * x


def seconds_conversion(sec: int) -> Tuple[int, int, int, int]:
    """
    The function takes a number of seconds as input.
    Returns a tuple: days, hours, minutes, seconds.

    """
    modulo = sec % 86400
    days = sec // 86400
    hours = modulo // 3600
    minutes = (modulo % 3600) // 60
    seconds = modulo % 60

    return days, hours, minutes, seconds


def sort_dict(dict_: dict) -> dict:
    """
    The function occupies an unsorted dictionary.
    Returns a dictionary sorted by keys.

    """
    return {key: dict_[key] for key in sorted(list(dict_.keys()))}


def tuple_processing(tuple_: tuple) -> int:
    """
    The function takes a tuple.
    Returns the length of all its words.

    """
    return len(''.join([word for word in tuple_ if isinstance(word, str)]))


def list_processing(list_: list) -> Tuple[int, int]:
    """
    The function accepts a list.
    Returns the number of digits and letters in it.

    """
    return (len([number for number in list_ if isinstance(number, int)]),
            len([j for line in list_ if isinstance(line, str) for j in line if j.isalpha()]))


def number_processing(number: int) -> int:
    """
    The function takes a number.
    Returns the number of odd digits.

    """
    return len([digit for digit in str(number) if int(digit) % 2 != 0])


def line_processing(str_: str) -> int:
    """
    The function takes a string.
    Returns the number of letters in a string.

    """
    return len([letter for letter in str_ if letter.isalpha()])


def multifunction(element: Union[Tuple, List, int, str]) -> Union[Tuple, int]:
    """
    The function accepts: a tuple, a list, a number, or a string.
    Returns: - if a tuple is the number of digits and letters in it;
             - if the list is the number of digits and letters in it;
             - if the number is the number of odd digits;
             - if string is the number of letters in the string.

    """
    result = None
    if isinstance(element, tuple):
        result = tuple_processing(element)

    elif isinstance(element, list):
        result = list_processing(element)

    elif isinstance(element, int):
        result = number_processing(element)

    elif isinstance(element, str):
        result = line_processing(element)

    return result


def test_multifunction(function, test_list):
    """
    The function takes a function name and a list with a collection.
    Outputs to the console the result of the function - ''multifunction()''.

    """
    for element in test_list:
        print(function(element))


print(f"Сумма n + nn + nnn: {number_conversion(int(input('Введите число: ')))}")

print(f'Количество гласных и согласных в этой строке соответственно: {even_and_odd_letters(input("Введите строку: "))}')

print(f"Y от X где X = -10 : +10 = {list(map(return_value_from_x, [i for i in range(-10, 11, 1)]))}")

print(seconds_conversion(100000))

print(sort_dict({100: 100, 1: 1, 0: 0, 5: 5, 4: 4, 3: 3, 2: 2}))

my_list = [[1, 2, 3, 44, 'python125'], ('hello', 'python', '5'), 22322, 'Hello Python', 55228]

test_multifunction(multifunction, my_list)
