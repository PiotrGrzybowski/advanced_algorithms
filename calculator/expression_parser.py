from typing import Dict

from calculator.number import Number
from calculator.operators import Operator, Associativity
from calculator.parenthesis import Parenthesis
from calculator.tokens import Token
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

        self.parse_to_postfix_expression()

    @property
    def current_char(self):
        return self.infix_expression[self.index]

    def parse_to_postfix_expression(self):
        while self.index < len(self.infix_expression):
            token = self.read_next_token()

            self.process_token(token)

        while len(self.tokens_stack) > 0:
            self.output_queue.push(self.tokens_stack.pop())

    def read_next_token(self):
        token = None

        if self._is_digit(self.current_char):
            token = self._build_next_number_token()
        elif self._is_operator(self.current_char):
            token = self._build_next_operator_token()
        elif self._is_parenthesis(self.current_char):
            token = self._build_next_parenthesis_token()
        # print(token.text)
        return token

    def process_token(self, token: Token):
        if isinstance(token, Number):
            self.output_queue.push(token)
        elif isinstance(token, Operator):
            self.process_operator_token(token)
        elif self.is_token_left_parenthesis(token):
            self.tokens_stack.push(token)
        elif self.is_token_right_parenthesis(token):
            self.process_right_parenthesis_token()


    def process_operator_token(self, operator: Operator):
        """
        (
            (there is a operator at the top of the operator stack)
             and
                (
                    (the operator at the top of the operator stack has greater precedence)
                      or
                    (the operator at the top of the operator stack has equal precedence and the token is left associative)
                )
             and
             (the operator at the top of the operator stack is not a left parenthesis)
        )
        """
        while len(self.tokens_stack) > 0 \
                and not self.is_token_left_parenthesis(self.tokens_stack.front()) \
                and ((self.tokens_stack.front().precedence > operator.precedence) or
                     (self.tokens_stack.front().precedence == operator.precedence and operator.associativity == Associativity.LEFT)):
            self.output_queue.push(self.tokens_stack.pop())
        self.tokens_stack.push(operator)

    def process_right_parenthesis_token(self):
        while not self.is_token_left_parenthesis(self.tokens_stack.front()):
            self.output_queue.push(self.tokens_stack.pop())

        if self.is_token_left_parenthesis(self.tokens_stack.front()):
            self.tokens_stack.pop()


    def is_token_left_parenthesis(self, token):
        if not isinstance(token, Parenthesis):
            return False
        else:
            return token.is_left()

    def is_token_right_parenthesis(self, token):
        if not isinstance(token, Parenthesis):
            return False
        else:
            return not token.is_left()

    def _build_next_number_token(self):
        start_index = self.index

        while self.index < len(self.infix_expression) and self._is_digit(self.current_char):
            self.index += 1

        number_text = self.infix_expression[start_index: self.index]

        return Number(number_text)

    def _build_next_operator_token(self):
        operator = self.operators[self.current_char]
        self.index += 1
        return operator

    def _build_next_parenthesis_token(self):
        parenthesis = self.operators[self.current_char]
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


