from abc import abstractmethod
from enum import Enum

from calculator.token import Token


class Associativity(Enum):
    LEFT = 1
    RIGHT = 2


class Operator(Token):
    def __init__(self, text: str, precedence: int, associativity: Associativity):
        super().__init__(text)
        self.precedence = precedence
        self.associativity = associativity

    @abstractmethod
    def evaluate(self, *args):
        pass


class Addition(Operator):
    def evaluate(self, number_1, number_2):
        return number_1 + number_2

    def __str__(self):
        return '+'
