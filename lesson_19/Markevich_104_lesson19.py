from typing import Union


def count_func(new_func):
    """
    Decorator function.
    The decorator outputs a number to the console -
    the number of values that are not multiples of the 'multiple' parameter of the 'look_for_multiples' function.

    """

    def wrapper(*args, **kwargs):
        nonlocal count
        result = new_func(*args, **kwargs)
        count = len(sum(args[0], [])) - len(result)
        print(f"Количество оставшихся элементов коллекции: {count}")
        return result

    count = 0
    return wrapper


def debug(func):
    """
    Decorator function.
    The decorator prints the name of the function to the console,
    (along with all arguments passed) and then what value she returns.

    """

    def wrapper(*args, **kwargs):
        print(f"Имя функции: {func.__name__}, "
              f"позиционные аргументы: {args if args else '-'}, "
              f"ключевые аргументы: {kwargs if kwargs else '-'}")
        result = func(*args, **kwargs)
        print(f"Функция возвращает: {result}, тип значения: {type(result)}")

        return result

    return wrapper


@debug
@count_func
def look_for_multiples(lst: list, multiple: int = 2) -> list:
    """
    The function takes a nested list and a 'multiple' parameter.
    Returns a list of multiples of the 'multiple' parameter.

    """
    return [j for i in lst for j in i if j % multiple == 0]


def test_look_for_multiples(func, new_multiple: int, dict_: dict) -> None:
    """
    Tests the 'look_for_multiples' function.

    """
    for key in dict_:
        print(f"\nИсходный список: {test_dict[key]}")
        print(func(dict_[key], new_multiple))


@debug
def calculate_the_sum(a: Union[int, float], b: Union[int, float], c: Union[int, float] = 0) -> int:
    """
    The function takes two positional arguments and one key argument.
    Returns the sum of numbers.

    """
    return a + b + c


@debug
def the_greater_of_the_two(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    The function takes two numbers.
    Returns the larger of two numbers.

    """
    return x if x > y else y


"""
Задача:
1. Дан список [[1,2,3], [4, 5, 6], [7, 8, 9]]
2. Напишите функцию, которая возвращает новый список, состоящий из значений кратных 3.
3. Напишите декоратор, который будет возвращать количество значений, не кратных 3 из вашей функции.

"""

# Определяем словарь для тестирования функции look_for_multiples и count_func
test_dict: dict = {1: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                   2: [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   3: [[1, 2, 3], [4, 5, 6]]
                   }

# Вызываем тест-функцию test_look_for_multiples
test_look_for_multiples(look_for_multiples, 3, test_dict)
print()

"""
Домашнее задание
Напишите декоратор debug, который при каждом вызове декорируемой функции 
выводит её имя (вместе со всеми передаваемыми аргументами), а затем — 
какое значение она возвращает. После этого выводится результат её выполнения.

"""

# Проверяем работу функции debug с функцией calculate_the_sum
print(calculate_the_sum(-10, 5, c=15))
print()

# Проверяем работу функции debug с функцией the_greater_of_the_two
print(the_greater_of_the_two(5, 100))
print()
print(the_greater_of_the_two(5, the_greater_of_the_two(100, 200)))
