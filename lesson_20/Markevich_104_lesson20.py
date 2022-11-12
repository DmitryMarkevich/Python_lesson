from time import sleep
from random import shuffle


class CardDeck(object):
    """A deck of playing cards."""

    RANKS: list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS: list = [" Трефы", " Бубны", " Червы", " Пики"]

    def __init__(self):
        self.cards = [j + i for i in self.SUITS for j in self.RANKS]
        self.map_index = 0

    def __iter__(self):
        self.card = ''
        return self

    def __next__(self):
        if self.map_index <= len(self.cards) - 1:
            self.card = self.cards[self.map_index]
            self.map_index += 1
            return self.card
        else:
            raise StopIteration

    def return_the_deck(self):
        """
        The method returns a deck of cards.

        """
        return self.cards

    def shuffle_the_deck(self):
        """
        The method shuffles the deck of cards.

        """
        shuffle(self.cards)


"""
Домашнее задание
Реализуйте итератор колоды карт (52 штуки) CardDeck.
Каждая карта представлена в виде строки типа «2 Пик».
При вызове функции next() будет представлена следующая карта. 
По окончании перебора всех элементов возникнет ошибка StopIteration.

"""

# Колода карт с индексом 1
cd_1 = CardDeck()
# Перемешаем колоду cd_1
cd_1.shuffle_the_deck()

# Выводим колоду cd_1 с помощью цикла for
print("Выводим в консоль всю колоду cd_1 с помощью цикла for: ")
for one_card in cd_1:
    print(one_card, end=' ')
    sleep(0.05)

print()
# Колода карт с индексом 2
cd_2 = CardDeck()
# Перемешаем колоду cd_2
cd_2.shuffle_the_deck()

# Выводим в консоль два раза по шесть карт из колоды cd_2
print("Два раза по шесть карт из колоды cd_2: ")
for _ in range(2):
    for _ in range(6):
        print(next(cd_2), end=' ')
    print()

print()
print("Еще шесть карт из колоды cd_2: ", end='')
print(next(cd_2), next(cd_2), next(cd_2), next(cd_2), next(cd_2), next(cd_2), end=' ')
