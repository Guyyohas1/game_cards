import random
from game_cards.Card import Card


class DeckOfCards:
    def init(self, deck: list):
        self.deck = []
        symbols = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for s in symbols:
            for v in range(13):
                deck.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        symbols = ["Spades", "Clubs", "Diamonds", "Hearts"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        random_symbols = random.choice(symbols)
        random_values = random.choice(values)
        random_card = random_symbols, random_values
       
        print(random_card)
        print(DeckOfCards)



