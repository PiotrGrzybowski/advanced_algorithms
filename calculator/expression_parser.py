from typing import Dict

from calculator.number import Number
from calculator.operators import Operator
from calculator.parenthesis import Parenthesis
from calculator.token import Token
from structures import Queue, Stack


class ExpressionParser:
    def __init__(self, operators: Dict[str, Token]):
        self.operators = operators
        self.infix_expression = None
        self.output_queue = Queue[Token]()
        self.tokens_stack = Stack[Token]()
        self.index = 0

    def evaluate_expression(self, expression: str):
        self.infix_expression = expression.replace(" ", "")
        self.index = 0
        self.output_queue.clear()

        self.parse_postfix_expression()

    def parse_postfix_expression(self):
        token = self.read_next_token()

        print(token.text)

    def read_next_token(self):
        token = None

        if self._is_digit(self.infix_expression[self.index]):
            token = self._build_next_number_token()
        elif self._is_operator(self.infix_expression[self.index]):
            token = self._build_next_operator_token()
        elif self._is_parenthesis(self.infix_expression[self.index]):
            token = self._build_next_parenthesis_token()

        return token

    def _build_next_number_token(self):
        start_index = self.index

        while self.index < len(self.infix_expression) and self._is_digit(self.infix_expression[self.index]):
            self.index += 1

        number_text = self.infix_expression[start_index: self.index]

        return Number(number_text)

    def _build_next_operator_token(self):
        operator = self.operators[self.infix_expression[self.index]]
        self.index += 1
        return operator

    def _build_next_parenthesis_token(self):
        parenthesis = self.operators[self.infix_expression[self.index]]
        self.index += 1
        return parenthesis

    def _is_digit(self, char):
        return char.isnumeric()

    def _is_operator(self, char):
        return char in self.operators.keys()

    def _is_parenthesis(self, char):
        return self._is_left_parenthesis(char) or self._is_right_parenthesis(char)

    def _is_left_parenthesis(self, char):
        return char == "("

    def _is_right_parenthesis(self, char):
        return char == ")"
