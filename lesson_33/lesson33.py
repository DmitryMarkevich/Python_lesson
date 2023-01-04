def factorial_recursive(number: int) -> int:
    """
    The function returns the factorial of a number.

    """
    try:
        return 1 if number == 1 else number * factorial_recursive(number - 1)

    except (RecursionError, TypeError):
        raise ValueError("Введите положительное число!")


def fibonacci_numbers(number: int) -> list:
    """
    The function returns Fibonacci numbers.

    """
    if number > 0:
        fibonacci_list = [1, 1]
        for i in range(2, number):
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

        return fibonacci_list
    else:
        raise Exception("Введите положительное число!")


n1 = int(input("Введите число: "))

print(f"Факториал числа {n1} равен: {factorial_recursive(n1)}")

n2 = int(input("Введите число: "))

print(f"Ряд Фибоначчи от 1 до {n2}: {fibonacci_numbers(n2)}")
