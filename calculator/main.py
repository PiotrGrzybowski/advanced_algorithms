from calculator.expression_parser import ExpressionParser
from calculator.operators import Addition, Associativity

addition = Addition(text='+', precedence=2, associativity=Associativity.LEFT)
operators = {addition.text: addition}

parser = ExpressionParser(operators=operators)
parser.evaluate_expression(" 12345  ")