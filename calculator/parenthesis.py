from calculator.operators import Associativity
from calculator.token import Token


class Parenthesis(Token):
    def __init__(self, text: str):
        super().__init__(text)
        self.associativity = self._evaluate_associativity()

    def _evaluate_associativity(self):
        if self.text == "(":
            return Associativity.LEFT
        else:
            return Associativity.RIGHT

    def __str__(self):
        return "(" if self.associativity == Associativity.LEFT else ")"
