def read_file(file_: str) -> list:
    """
    The function accepts a target file for reading data.
    Returns a list with numbers in ascending order, followed by strings in ascending order of their length.

    """
    try:
        with open(file_, 'r', encoding='utf-8') as file:
            result_list = []
            for i in file:
                result_list.append(i.strip().split())

            return result_list

    except FileNotFoundError:
        print("Невозможно открыть файл.")


def list_of_numbers(list_: list) -> list:
    """
    The function takes a nested list, the elements of nested lists are numbers in str format.
    Returns a list in which nested lists contain numbers.

    """

    return [[int(j) for j in i] for i in list_]


def add_diagonals(list_: list) -> list:
    """
    The function accepts a list with nested lists,
    the elements of the nested lists are the numbers of the magic square.
    Generates list with diagonal numbers and adds them to the original list.
    Returns the resulting list.

    """
    new_list = list_[:]
    diagonal_elements_1, diagonal_elements_2 = [], []
    index_ = 0
    for i in new_list:
        diagonal_elements_1.append(i[index_])
        diagonal_elements_2.append(i[len(i) - 1 - index_])
        index_ += 1
    new_list.append(diagonal_elements_1)
    new_list.append(diagonal_elements_2)

    return new_list


def check_square_1(lst_: list) -> bool:
    """
    The function takes a list whose elements are magic square numbers.
    Returns True if magic square, False otherwise.

    """
    flag = True
    s = sum(lst_[0])
    for i in range(1, len(lst_) - 1):
        flag = flag and s == sum(lst_[i])

    return flag


# Второй вариант функции check_square_
def check_square_2(lst_: list) -> bool:
    """
    The function takes a list whose elements are magic square numbers.
    Returns True if magic square, False otherwise.

    """
    n = len(lst_[0])
    magic_constant = (n * (n ** 2 + 1)) / 2

    return all([magic_constant == sum(i) for i in lst_])


def main():
    """
    main function.

    """
    file = 'magic_square.txt'
    try:
        square_list = list_of_numbers(read_file(file))
        list_with_diagonals = add_diagonals(square_list)

        print(f"Квадрат в файле '{file}'"
              f" {'является' if check_square_2(list_with_diagonals) else 'не является'}"
              f" магическим квадратом.")

    except ValueError:
        print(f"Похоже Вы ввели некорректные данные: {read_file(file)}")


main()

# В файле 'magic_square.txt' имеем данные представленные в следующем виде:
"""
7 12 1 14
2 13 8 11
16 3 10 5
9 6 15 4
"""
