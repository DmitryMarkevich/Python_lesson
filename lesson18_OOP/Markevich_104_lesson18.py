from random import choice
from typing import Union


class Tomato(object):
    """Class for creating a Tomato object."""
    states: dict = {1: "образование бутонов",
                    2: "цветение",
                    3: "формирование плодов",
                    4: "созревание плодов",
                    5: "плод созрел"
                    }

    def __init__(self, index: Union[int, float], state: int = states[1]) -> None:
        self._index = index
        self._state = state

    def grow(self) -> None:
        """The method transfers the tomato fruit to the next stage of ripening."""
        for st in self.states:
            if self._index == st:
                self._state = self.states[st]
                break

    def is_ripe(self) -> bool:
        """The method returns True if the fruit is ripe otherwise False."""
        if self._state == self.states[5]:
            return True
        else:
            return False

    def index_plus_minus(self, new_index: Union[int, float], parameter=True) -> None:
        """The method corrects the object's '_index' property."""
        if parameter:
            self._index += new_index
        else:
            self._index -= new_index

    def condition(self):
        """The method returns the object's '_state' property."""
        return self._state


class TomatoBush(object):
    """Class for creating a TomatoBush object."""

    def __init__(self, count: int) -> None:
        self.tomatoes = []
        for i in range(count):
            self.tomatoes.append(Tomato(choice([0.5, 1])))

    def grow_all(self) -> None:
        """The method iterates through the list of tomatoes and transfers them to the next stage of ripening."""
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        """The method returns True if all fruits are ripe, False otherwise."""
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self) -> None:
        """The method clears the list containing the tomato objects if they are all ripe."""
        if self.all_are_ripe():
            self.tomatoes.clear()


class Gardener(object):
    """Class for creating a Gardener object."""
    count: int = 0
    number_of_tomatoes: int = 0

    def __init__(self, name: str, plant=TomatoBush(choice([*range(5, 11, 1)]))) -> None:
        self.name = name
        self._plant = plant
        self.count_objects()

    @classmethod
    def count_objects(cls) -> None:
        """The method increments the 'count' attribute."""
        cls.count += 1

    def work(self) -> None:
        """The method increments the tomato's '_index' property by the given value."""
        for tomato in self._plant.tomatoes:
            tomato.index_plus_minus(0.5)
        self._plant.grow_all()

    def check_the_harvest(self) -> bool:
        """The method checks the maturation of the crop."""
        if self._plant.all_are_ripe():
            return True
        else:
            return False

    def harvest(self) -> None:
        """The method assigns the crop amount to the number_of_tomatoes class attribute and
        clears the list of Tomato objects."""
        self.number_of_tomatoes = self.len_tomatoes()
        self._plant.give_away_all()

    def len_tomatoes(self) -> int:
        """The method returns the number of Tomato objects."""
        return len(self._plant.tomatoes)

    @staticmethod
    def knowledge_base(name: str, count: int, len_tomato: int) -> None:
        """The method returns help for the gardener."""
        print(f"*** Привет! я садовник. Меня зовут {name} ***\n"
              f"*** У меня в огороде {count} куст томата. ***\n"
              f"*** На котором {len_tomato} помидор. ***\n")

    def output_in_detail_by_tomatoes(self) -> None:
        """The method outputs the current maturation stage of Tomato objects to the console."""
        count = 1
        for tomato in self._plant.tomatoes:
            print(f"{count} томат находится на стадии: {tomato.condition()}")
            count += 1


def main():
    gardener = Gardener('Thomas')

    while True:
        print("""Это игра 'САДОВНИК'
        
        Меню игры:
                1 - справка по садовнику
                2 - полить томатный куст
                3 - подкормить томатный куст
                4 - проверить плоды
                5 - вывести справку по плодам
                6 - собрать урожай
                7 - покинуть огород
                """)

        rec = input("Выберите действие: ")

        if rec == '1':
            gardener.knowledge_base(gardener.name, gardener.count, gardener.len_tomatoes())

        elif rec == '2':
            if gardener.len_tomatoes() != 0:
                print(choice(["Своевременный полив это очень важно.\n",
                              "Без воды огород не вырастишь.\n",
                              "Хороший хозяин всегда следит за влажностью почвы.\n"]))

                gardener.work()

            else:
                print(f"Вы уже собрали весь урожай томатов в количестве: {gardener.number_of_tomatoes} шт.\n")

        elif rec == '3':
            if gardener.len_tomatoes() != 0:
                print(choice(["Без удобрений растение не сможет нормально развиваться.\n",
                              "Удобрение - основа растениеводства!\n",
                              "Хорошо подкормил - собрал богатый урожай.\n"]))

            else:
                print(f"Вы уже собрали весь урожай томатов в количестве: {gardener.number_of_tomatoes} шт.\n")

            gardener.work()

        elif rec == '4':
            if gardener.check_the_harvest():
                print("Похоже, что все плоды созрели.\n")
            else:
                print("Плоды еще не созрели.\n")

        elif rec == '5':
            gardener.output_in_detail_by_tomatoes()

        elif rec == '6':
            if gardener.number_of_tomatoes == 0:
                if gardener.check_the_harvest():
                    gardener.harvest()
                    print(f"Мы собрали хороший урожай томатов! В количестве {gardener.number_of_tomatoes} шт.\n")
                else:
                    print("К сожелению плоды еще не созрели.\n")
            else:
                print(f"Вы уже собрали весь урожай томатов в количестве: {gardener.number_of_tomatoes} шт.\n")

        elif rec == '7':
            print("До свидания.")
            break

        else:
            print("Такого пункта в меню нет.\n")


# Запускаем игру
main()
