from calculator.expression_parser import ExpressionParser
from calculator.operators import Addition, Associativity, Subtraction, Multiplication, Division, Power
from calculator.parenthesis import Parenthesis

addition = Addition(text='+', precedence=2, associativity=Associativity.LEFT)
subtraction = Subtraction(text='-', precedence=2, associativity=Associativity.LEFT)
multiplication = Multiplication(text='*', precedence=3, associativity=Associativity.LEFT)
division = Division(text='/', precedence=3, associativity=Associativity.LEFT)
power = Power(text='^', precedence=4, associativity=Associativity.RIGHT)

left_parenthesis = Parenthesis("(")
right_parenthesis = Parenthesis(")")

operators = {
    addition.text: addition,
    subtraction.text: subtraction,
    multiplication.text: multiplication,
    division.text: division,
    power.text: power,

    left_parenthesis.text: left_parenthesis,
    right_parenthesis.text: right_parenthesis,
}

parser = ExpressionParser(operators=operators)
parser.evaluate_expression("123 + 12 /   8   -   (   12  ^ 5) ")