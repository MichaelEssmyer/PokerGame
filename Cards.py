#stack overflow
import random

class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def getRank(self):
        return self.rank

    def getSuite(self):
        return self.suite

    def Value(self):
        if self.rank == 'Ace':
            return 14
        elif self.rank == 'Jack':
            return 11
        elif self.rank == 'Queen':
            return 12
        elif self.rank == 'King':
            return 13
        else:
            return int(self.rank)

    def __str__(self):
        return ('{0} of {1}'.format(self.rank, self.suite))


def shuffled_deck():
    deck = []
    for suite in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
        for num in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            deck.append([num, suite])
    random.shuffle(deck)
    return deck
