import collections
import random

Card = collections.namedtuple('Card', ['suit', 'rank'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, pos):
        return self.cards[pos]


cards = FrenchDeck()
for n in range(10):
    print(random.choice(cards))
