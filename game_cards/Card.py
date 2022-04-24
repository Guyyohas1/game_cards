class Card:
    def __init__(self, symbol, value: int):
        self.symbol = symbol
        self.value = value

    def __gt__(self, other):
        return self.value > other.value
