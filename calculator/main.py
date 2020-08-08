from calculator.expression_parser import ExpressionParser
from calculator.operators import Addition, Associativity
from calculator.parenthesis import Parenthesis

addition = Addition(text='+', precedence=2, associativity=Associativity.LEFT)
subtraction = Addition(text='-', precedence=2, associativity=Associativity.LEFT)
multiplication = Addition(text='*', precedence=3, associativity=Associativity.LEFT)
division = Addition(text='/', precedence=3, associativity=Associativity.LEFT)
power = Addition(text='^', precedence=4, associativity=Associativity.RIGHT)

left_parenthesis = Parenthesis("(")
right_parenthesis = Parenthesis(")")

operators = {
    addition.text: addition,

    left_parenthesis.text: left_parenthesis,
    right_parenthesis.text: right_parenthesis,
}

parser = ExpressionParser(operators=operators)
parser.evaluate_expression(" )  ")