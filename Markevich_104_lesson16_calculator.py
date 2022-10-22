from typing import Tuple, Union


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


def give_sum(a: Union[int, float], b: Union[int, float]) -> float:
    """
    The function takes two arguments and returns their sum.

    """
    return a + b


def give_minus(a: Union[int, float], b: Union[int, float]) -> float:
    """
    The function takes two arguments and returns their difference.

    """
    return a - b


def give_multiplication(a: Union[int, float], b: Union[int, float]) -> float:
    """
    The function takes two arguments and returns their product.

    """
    return a * b


def action_output(a: int, s: str, b: int, f) -> None:
    """
    The function takes four arguments: the number a, the sign of the mathematical operation,
    the number b and the function of the mathematical operation.
    Prints a mathematical operation with a result to the console.

    """

    print(f"{a} {s} {b} = {f(a, b)}\n")


def menu_display() -> None:
    """
    The function displays the program menu in the console.

    """
    print("""Программа 'КАЛЬКУЛЯТОР'
             0 - Выйти
             1 - Запустить программу
          """
          )


def user_input(option=True) -> Tuple[str] or Tuple[str, str, str]:
    """
    The function takes user input and returns it.

    """
    if option:
        menu = input("Ваш выбор: ")

        return menu

    else:
        first_number, sign, second_number = input("Введите первое число: "), \
                                            input("Введите знак (* / + -): "), \
                                            input("Введите второе число: ")

        return first_number, sign, second_number


def main():
    """
    The main block of code is placed in the main() function.

    """

    function_dictionary = {'+': give_sum, '-': give_minus, '*': give_multiplication, '/': give_division}

    choice = None

    while choice != 0:
        # Вывод меню программы
        menu_display()
        choice = user_input()  # Принимаем ввод пользователя
        print()
        # Выход
        if choice == "0":
            print("До свидания.")
            break
        # Запуск программы
        elif choice == "1":
            flag = True
            while flag:
                try:
                    # Принимаем ввод пользователя
                    int_1, sign, int_2 = user_input(option=False)
                    # Если не число бросаем исключение
                    if not int_1.replace('.', '').isdigit() and not int_2.replace('.', '').isdigit():
                        raise ValueError("Аргументы должны быть числом.")
                    # Если некорректный знак - бросаем исключение
                    if sign not in function_dictionary:
                        raise KeyError("Неправильный знак математической операции.")
                    # Преобразовываем str в float
                    int_1, int_2 = float(int_1), float(int_2)
                    # Выполняем вычисление
                    action_output(int_1, sign, int_2, function_dictionary[sign])
                    flag = False

                # Перехватываем исключения
                except (ValueError, ZeroDivisionError, KeyError) as exc:
                    print(exc)
                    flag = True

        else:
            print(f"Извините, в меню нет пункта {choice}")
    print()


# Запуск программы калькулятор
main()
