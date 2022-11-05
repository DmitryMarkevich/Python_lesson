from typing import Union
from textwrap import dedent
import string


class Human(object):
    """Class for creating a Human object."""
    default_name: str = 'Thomas'
    default_age: int = None

    def __init__(self, name: str = default_name, age: int = default_age) -> None:
        self.name = name
        self.age = age
        self._money = 0
        self._house = None

    def info(self) -> Union[str, int, int, object]:
        """The method returns the attribute values of the Human object."""
        return self.name, self.age, self._money, self._house

    def earn_money(self, money: float) -> float:
        """The method increments the _money object attribute by the passed value."""
        self._money += money

    def _make_deel(self, house: object, price: float) -> None:
        """The method simulates buying a house: it decrements the _money object property and
        keeps a reference to the House object."""
        self._money -= price
        self._house = house

    def buy_house(self, house: object, price: float) -> None:
        """The method checks the solvency of the Human object."""
        if self._money >= price:
            self._make_deel(house, price)
        else:
            print("You don't have enough funds.")

    @classmethod
    def default_info(cls) -> Union[str, int]:
        """The method returns the value of the attributes of the Human class as a tuple."""
        return cls.default_name, cls.default_age


class House(object):
    """Class for creating a House object."""

    def __init__(self, area: float, price: float) -> None:
        self._area = area
        self._price = price

    def final_price(self, discount: Union[int, float]) -> float:
        """The method returns the final cost of the house, including the discount."""
        return round(self._price * (1 - discount / 100), 2)


class SmallHouse(House):
    """Class for creating a SmallHouse object."""

    MIN_AREA: float = 40
    STARTING_PRICE: float = 0

    def __init__(self, area: float = MIN_AREA, price: float = STARTING_PRICE) -> None:
        super().__init__(area, price)


class Alphabet(object):
    """Class for creating an Alphabet object."""

    def __init__(self, lang: str, letters: str) -> None:
        self.lang = lang
        self.letters = list(letters)

    def print(self) -> None:
        """The method prints the value of the 'letters' property to the console."""
        print(*self.letters, sep=',')

    def letters_num(self) -> int:
        """The method returns the number of elements in the collection of the 'letters' property."""
        return len(self.letters)


class EngAlphabet(Alphabet):
    """Class for creating an EngAlphabet object."""
    _letters_num: int = 0

    def __init__(self, lang: str, letters: str) -> None:
        super().__init__(lang, letters)
        self.count_letters(letters)

    @classmethod
    def count_letters(cls, letters: str) -> None:
        """The method assigns a value to the '_letters_num' class attribute."""
        cls._letters_num = len(letters)

    def in_en_letter(self, letter: str) -> bool:
        """The method returns True if the passed character is in the object's 'letters' attribute,
        otherwise False."""
        return letter.lower() in self.letters

    @classmethod
    def letters_num(cls) -> int:
        """The method returns the value of the _letters_num class attribute."""
        return cls._letters_num

    @staticmethod
    def example() -> str:
        """The method returns an example text in English."""
        return dedent("""
        I usually have four meals a day. In the morning I have breakfast.
        At school I have lunch. At home I have dinner and in the evening I have supper. 
        Besides, I like to eat an apple or a banana,  
        or to drink a glass of juice between meals, if I'm thirsty.
        """)


h = House(50, 120)
print(f"Словарь атрибутов объекта класса House: {h.__dict__}\n"
      f"Цена с учетом скидки в 50% {h.final_price(50)}\n")

sh = SmallHouse(40, 100)
print(f"Словарь атрибутов объекта класса SmallHouse: {sh.__dict__}\n")

a = Human("Alex", 25)
print(f"Выводим в консоль информацию по объекту класса Human: {a.default_info()}\n")
print(f"Выводим в консоль все атрибуты объекта класса Human: {a.info()}\n")

print("Увеличиваем значение атрибута '_money' объекта класса Human на 500 у.е.")
a.earn_money(500)
print(f"Теперь атрибуты объекта класса Human такие: {a.info()}\n")

print("Покупаем дом стоимостью 100 у.е.")
a.buy_house(sh, 100)
print(f"Выводим в консоль атрибуты объекта класса Human после покупки: {a.info()}\n")

print("Создаем объект класса Alphabet.")
a = Alphabet('eng', string.ascii_lowercase)
print("Выводим в консоль значение атрибута 'letters' объекта класса Alphabet:")
a.print()
print(f"Количество значений в атрибуте 'letters' объекта класса Alphabet: {a.letters_num()}\n")

print("Создаем объект класса EngAlphabet.")
an = EngAlphabet('eng', string.ascii_lowercase)
print("Выполняем проверку методов класса EngAlphabet.")
print(f"Проверка метода letters_num: {an.letters_num()}\n"
      f"Проверка метода in_en_letter с символом 'z': {an.in_en_letter('z')}\n"
      f"Проверка метода in_en_letter с символом 'Z': {an.in_en_letter('Z')}\n"
      f"Проверка метода in_en_letter с символом 'А': {an.in_en_letter('А')}\n"
      f"Проверка метода example:{an.example()}")

