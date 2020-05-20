import Card

class Hand():
    def __init__(self, Card):
        self.cards = Card.shuffled_deck()

def makeHand(size):
    hand = []
    for i in range(size):
        hand.append(cards[i])
    return hand
