from calculator.tokens import Token


class Number(Token):
    def __init__(self, text):
        super().__init__(text)

        self.value = float(self.text)

    def __str__(self):
        return self.text

    # def __add__(self, other):
    #     pass
    #
    # def __mul__(self, other):
    #     pass
    #
    # def __sub__(self, other):
    #     pass
    # def __po