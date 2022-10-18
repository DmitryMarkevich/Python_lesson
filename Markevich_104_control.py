from typing import Union, Tuple
from datetime import datetime, timedelta


# Задача №1
def body_mass_index(weight: float, growth: float) -> float:
    """
    The function accepts the mass and height of a person.
    Returns the body mass index.

    """
    return round(weight / growth ** 2, 2)


def body_mass_index_processing(index: float) -> None:
    """
    The function accepts a body mass index.
    Returns the BMI characteristic to the console.

    """
    if index < 25:
        print("У Вас все хорошо.")
    elif 25 <= index < 30:
        print("Вы имеете избыточный вес! Пора в спортзал.")
    else:
        print("Нет, ну разве можно столько кушать?")


# Задача №2
def define_figure(int_: int) -> None:
    """
    The function takes a number - the number of sides of the geometric figure.
    Prints the name of the geometric figure to the console.

    """
    dict_figure = {3: 'треугольник',
                   4: 'квадрат',
                   5: 'пятиугольник',
                   6: 'шестиугольник',
                   7: 'семиугольник',
                   8: 'восьмиугольник',
                   9: 'девятиугольник',
                   10: 'многогранник',
                   }
    if int_ in dict_figure:
        for key in dict_figure:
            if key == int_:
                print(f"Это фигура: {dict_figure[key].upper()}")
    else:
        print("Вы ввели некорректные данные.")


# Задача №3
def next_date(when: str) -> str:
    """
    The function takes a date as an argument.
    Returns the next date in the calendar.

    """
    dt = datetime.strptime(when, '%Y-%m-%d')
    result = dt + timedelta(days=1)
    return result.strftime('%Y-%m-%d')


# Задача №4
def delivery_calculation(amount: int,
                         service_price_1: float = 10.95,
                         service_price_2: float = 2.95) -> float:
    """
    The function takes an integer - the quantity of goods.
    Returns the shipping cost based on the quantity of the item.

    """

    return round(service_price_1 + (amount - 1) * service_price_2, 2)


# Задача №5
def fraction_reduction(numerator: int, denominator: int) -> Union[int, Tuple[int, int]]:
    """
    The function takes two numbers: the numerator and denominator of the fraction.
    Returns the reduced fraction as a tuple.

    """
    divider = 1
    min_int = min(numerator, denominator)

    while divider <= min_int:
        if numerator % divider == 0 and denominator % divider == 0:
            numerator /= divider
            denominator /= divider
            divider = 1
        divider += 1

    return numerator if numerator == denominator else (numerator, denominator)


def test_fraction_reduction() -> None:
    """
    fraction_reduction() function test.

    """
    arguments = int(input("Введите числитель дроби: ")), int(input("Введите знаменатель дроби: "))
    result = fraction_reduction(*arguments)

    if isinstance(result, tuple):
        print(f"{int(result[0])}/{int(result[1])}")

    else:
        print(f"{int(result)}")


# Задача №6
def list_output(lst: list) -> None:
    """
    The function takes a list of numeric and string data.
    Prints list processing options to the console.

    """
    print(lst[::-1],
          sorted([i for i in lst if isinstance(i, int)], reverse=True) +
          sorted([i for i in lst if isinstance(i, str)], reverse=True),
          sorted([i for i in lst if isinstance(i, int)]) +
          sorted([i for i in lst if isinstance(i, str)]),
          lst[2:7],
          [st for st in lst if lst.index(st) != 4],
          set(lst),
          [i for i in lst if isinstance(i, int)], sep='\n')


# Задача №7
def count_range(list_: list,
                bottom_line: Union[int, float],
                upper_bound: Union[int, float]) -> int:
    """
    The function takes a list, lower and upper bounds of the sequence.
    Returns the number of elements in the given range.

    """

    return sum([1 for _ in list_ if bottom_line <= _ < upper_bound])


def test_count_range(test_list: list, argument_list: list) -> None:
    """
    The function takes a list and arguments to test.
    Returns the test results.

    """
    for a, b in zip(test_list, argument_list):
        print(count_range(a, *b))


# Задача №8
def count_list(list_: list) -> int:
    """
    The function accepts a multidimensional list.
    Returns the number of nested lists.

    """
    result = 0
    for i in list_:
        if isinstance(i, list):
            result += 1
            result += count_list(i)

    return result


# Задача №9
def anagram(word_1: str, word_2: str) -> bool:
    """
    The function takes two words.
    Returns True if the words are anagrams, False otherwise.

    """
    return sorted(word_1.lower()) == sorted(word_2.lower())


def test_anagram() -> None:
    """
    anagram() function test.

    """
    arguments = input("Введите первое слово: "), input("Введите второе слово: ")

    if anagram(*arguments):
        print("Введенные слова являются анаграммами.")
    else:
        print("Введенные слова не являются анаграммами.")


# Задача №10
def converting_letters_to_numbers_1(str_: str, dict_: dict) -> str:
    """
    The function takes a string.
    Returns the numeric representation of a string based on the dictionary data.

    """
    new_str = ''
    for symbol in str_.upper():
        for key in dict_:
            if symbol in key:
                new_str += str(dict_[key]) * (key.index(symbol) + 1)

    return new_str


def converting_letters_to_numbers_2(str_: str, dict_: dict) -> str:
    """
    The function takes a string.
    Returns the numeric representation of a string based on the dictionary data.

    """
    return ''.join([(str(dict_[key]) * (key.index(st) + 1))
                    for st in str_.upper()
                    for key in dict_
                    if st in key])


# Задача №11
def recursive_flatten_generator(array: list) -> list:
    """
    The function takes a multidimensional list as an argument.
    Returns a flat (one-dimensional) list.

    """
    lst = []
    for i in array:
        if isinstance(i, list):
            lst.extend(recursive_flatten_generator(i))
        else:
            lst.append(i)

    return lst


# Задача №1
print("Задача №1")
ind = body_mass_index(float(input("Введите массу тела в кг: ")),
                      float(input("Введите рост в м: ")))

body_mass_index_processing(ind)
print()

# Задача №2
print("Задача №2")
define_figure(int(input("Введите количество сторон фигуры (от 3 до 10): ")))
print()

# Задача №3
print("Задача №3")
print(f"""Следующая дата будет: {next_date(input("Введите исходную дату в формате '2020-12-12': "))}""")
print()

# Задача №4
print("Задача №4")
print(f"Стоимость доставки: {delivery_calculation(int(input('Введите количество товара: ')))}")
print()

# Задача №5
print("Задача №5")
test_fraction_reduction()
print()

# Задача №6
print("Задача №6")
test_list_1 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 2]
list_output(test_list_1)
print()

# Задача №7
print("Задача №7")
my_test_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [11, 12, 13, 14, 15, 16, 17, 18, 19],
                [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]]

my_argument_list = [[2, 5], [11, 13], [1.5, 2]]

test_count_range(my_test_list, my_argument_list)
print()

# Задача №8
print("Задача №8")
my_lst = [[], [], [[], [[[]]]]]

print(count_list(my_lst))
print()

# Задача №9
print("Задача №9")
test_anagram()
print()

# Задача №10
print("Задача №10")
translation_dictionary = {'.,?!:': 1, 'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5,
                          'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9, ' ': 0
                          }

line = input("Введите строку: ")

print(converting_letters_to_numbers_1(line, translation_dictionary))
print(converting_letters_to_numbers_2(line, translation_dictionary))
print()

# Задача №11
print("Задача №11")
multidimensional_list = [1, 2, 'stroka', [[2, 2, [1, [2]], 'st'], 2, 3, 'str']]

print(recursive_flatten_generator(multidimensional_list))
