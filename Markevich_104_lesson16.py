from typing import Union


def give_division(number_1: Union[int, float], number_2: Union[int, float]) -> float:
    """
    The function takes two numbers.
    Returns the quotient of division.

    """
    if not isinstance(number_1, float) or not isinstance(number_2, float):  # Проверка, что переданные аргументы - числа
        raise ValueError("Аргументы должны быть числом.")

    if number_2 == 0:  # Проверка если делитель равен нулю
        raise ZeroDivisionError("Делитель не может быть равен нулю.")

    return number_1 / number_2


def main():
    """
    The main block of code is placed in the main() function.

    """
    flag = True
    while flag:
        try:
            # Принимаем ввод пользователя
            int_1, int_2 = float(input("Введите первое число: ")), float(input("Введите второе число: "))
            # Выполняем вычисление
            print(give_division(int_1, int_2))
            flag = False

        except (ValueError, ZeroDivisionError) as exc:
            print(exc)
            flag = True


# Запуск программы
main()
