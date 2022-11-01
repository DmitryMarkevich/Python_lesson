from typing import Union


class Analyzer(object):
    """
    Analyzer class.
    With the help of this class, objects are created for parsing data of type str b int.

    """

    def __init__(self, value: Union[str, int]) -> None:
        self.value = value
        self.length_value = self.element_length(value)
        self.analysis = self.parse_property()

    def element_length(self, y: Union[str, int]) -> int:
        """
        The method takes one argument.
        If the argument is a string or a number,
        returns the length of the string or number, respectively.

        """

        if isinstance(y, str):
            return len(y)
        elif isinstance(y, int):
            return len(str(y))
        else:
            return None

    def parse_property(self) -> Union[str, int]:
        """
        The method parses the object's value property.

        If the object property is a string,
        returns all vowels if the product of vowels and consonants less than or equal to word length,
        otherwise returns consonants.

        If the object property is a number,
        returns the product of the sum of even digits to the length of this number.

        """

        data: dict = {"aeiou": '',
                      "bcdfghjklmnpqrstvwxyz": ''
                      }

        if isinstance(self.value, str):
            for element in self.value.lower():
                for key in data:
                    if element in key:
                        data[key] += element

            if len(data["aeiou"]) * len(data["bcdfghjklmnpqrstvwxyz"]) <= self.length_value:

                return data["aeiou"]
            else:
                return data["bcdfghjklmnpqrstvwxyz"]

        elif isinstance(self.value, int):

            return sum([int(i) for i in str(self.value) if int(i) % 2 == 0]) * self.length_value

        else:

            return None


def test_analyzer():
    """
    The function tests the Analyzer class.

    """
    for elem in [125, 18, 'Pythonist', 'hello', 25, 111, 'list', 22, 'values', 'person', 88]:
        analyze_1 = Analyzer(elem)
        print(f"self.value = {analyze_1.value}, self.analysis =  {analyze_1.analysis}\n")


test_analyzer()
