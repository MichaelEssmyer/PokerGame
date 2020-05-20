import Cards

class Deck:
    def __init__(self):
        self.deck = [Cards.shuffled_deck()]

        
def make_hand(hand_size):
    DealerHand = []
    for i in range(hand_size):
        DealerHand.append(deck[i])
    return DealerHand 
