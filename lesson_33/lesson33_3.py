def remove_punctuation_marks(base_string: str, element: str) -> str:
    """
    The function takes a string as input.
    Returns the original string with all punctuation removed.

    """
    return ''.join([j for j in base_string if j not in element])


def remove_upper_case(base_string: str) -> str:
    """
    The function takes a string as input.
    Returns the original string with the uppercase letters removed.

    """
    new_string = ''
    for element in base_string:
        if element == element.lower():
            new_string += element

    return new_string


def convert_to_upper_case(base_string: str) -> str:
    """
    The function takes a string as input.
    Returns the original string converting all characters to uppercase.

    """
    return base_string.upper()


def change_case(base_string: str) -> str:
    """
    The function takes a string as input.
    Returns the original string with the letter case reversed.

    """
    return base_string.swapcase()


def replace_punctuation_marks(base_string: str, element: str, new_element: str = ' ') -> str:
    """
    The function takes a string as input.
    Returns the original string, replacing punctuation with a space.

    """
    return ''.join([i if i not in element else new_element for i in base_string])


# **************************************************************************************************

original_string = "Что это было?... Я не ожидал увидеть подобного, но мне придётся принять решение."

punctuation_marks = '''.,?!:;'''

print("Выводим всю строку без знаков препинания: ",
      remove_punctuation_marks(original_string, punctuation_marks), sep='\n')

print("Выводим строку без букв верхнего регистра: ",
      remove_upper_case(original_string), sep='\n')

print("Выводим всю строку в верхнем регистре: ",
      convert_to_upper_case(original_string), sep='\n')

print("Выводим всю строку изменив регистр букв на противоположный: ",
      change_case(original_string), sep='\n')

print("Выводим всю строку заменив знаки препинания на пробел: ",
      replace_punctuation_marks(original_string, punctuation_marks), sep='\n')
