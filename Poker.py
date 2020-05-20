import Card
import Math

class Poker:
    
    def __init__(self, hand, score):
        self.hand = hand
        self.score - score
        
    def getHand(self):
        return self.hand
    
    def getScore(self):
        return self.score                   
    
    def check_hand(self, hand, comm):
       maxscore = calculate_score(hand, comm)
       if maxscore > self.score:
             self.score = maxscore

    def calculate_score(hand, comm):
        '''Check functions calculate the probablity of hand occuring for the win'''
        highProb = check_highCard(hand, comm)
        oneProb = check_onePair(hand, comm)
        twoProb = check_twoPair(hand, comm)
        threeProb = check_threeKind(hand, comm)
        straightProb = check_straight(hand, comm)
        flushProb = check_flush(hand, comm)
        fullProb = check_fullHouse(hand, comm)
        fourProb = check_fourKind(hand, comm)
        straightFlushProb = check_straightFlush(hand, comm)

    def check_highCard(hand, comm):
        '''High card. Does not qualify for any higher rank.
        Ties are broken between these hands by comparing the highest card (Ace counts as high.)
        If the first cards match, go down to thesecond-highest card, etc'''
        prob1 = (math.factorial(hand[1].Value)/math.factorial(5))((math.factorial(4))^5-4)
        prob2 = (math.factorial(hand[2].Value)/math.factorial(5))((math.factorial(4))^5-4)
        if prob1 >= prob2:
            return prob1
        else:
            return prob2
        
    def check_onePair(hand, comm):
        '''One pair. 2 cards of the same rank; the other 3 cards are of different ranks.
        Ties between these hands are broken by comparing the value of the pair, higher value wins.
        If both are the same value, the tie is broken by looking at the highest of the remaining cards, then second-highest if necessary, etc.'''
        for i in 2:
            for j to 5:
                if i == j:
                    break
                else:
                    if hand[i] == hand[j]:
                        prob1 = (math.factorial(13)/math.factorial(1))(math.factorial(hand[i].Value)/math.factorial(2))(math.factorial(12)/math.factorial(3))(math.factorial(hand[j].Value)/math.factorial(1))^3
                if hand[i] == comm[j]:
                    prob2 = (math.factorial(13)/math.factorial(1))(math.factorial(hand[i].Value)/math.factorial(2))(math.factorial(12)/math.factorial(3))(math.factorial(comm[j].Value)/math.factorial(1))^3
        if prob1 >= prob2:
            return prob1
        else:
            return prob2
        
    def check_twoPair(hand):
        ''' Two pair. 2 cards of the same rank, 2 cards of another rank, and an unmatched ‘side’ card.
        Ties are broken by comparing the higher pairs; then if necessary the lower pairs, then the side cards.'''
        for i in 2:
            for x in 2:
                for j to 5:
                    for y to 5:
                        if i == x or j == y:
                            break
                        else:
                            if hand[i] == hand[j] and hand[x] == hand[y]:
                                prob1 = (math.factorial(13)/math.factorial(2))(math.factorial(hand[i].Value)/math.factorial(2))^2(math.factorial(11)/math.factorial(3))(math.factorial(hand[j].Value)/math.factorial(1))
                            if hand[i] == comm[j] and hand[x] == comm[y]:
                                prob2 = (math.factorial(13)/math.factorial(2))(math.factorial(hand[i].Value)/math.factorial(2))^2(math.factorial(11)/math.factorial(3))(math.factorial(comm[j].Value)/math.factorial(1))
        if prob1 >= prob2:
            return prob1
        else:
            return prob2
        
    def check_threeKind(hand):
        ''' Three of a kind. 3 cards of the same rank, and 2 unrelated side cards.
        Ties are broken by comparing the value of the 3 matching cards.'''
        for i in 2:
            for j in 5:
                for k in 5:
                    if j == k:
                        break
                        if hand[i] 

    def check_straight(hand):
        ''' Straight. 5 cards in unbroken sequence, not all the same suit.
        Ties broken by looking at the highest card in the sequence.
        Ace can be low (5-4-3-2-A) or high (A-K-Q-J-10), but can’t go “around the corner,” i.e. 3-2-A-K-Q is NOT a straight.
        (It’s a high-card hand unless it’s a flush.)'''

    def check_flush(hand):
        ''' Flush. All 5 cards are the same suit.
        Ties broken by rank of highest card, then second highest if needed, etc.'''

    def check_fullHouse(hand):
        ''' Full House. 3 matching cards of 1 rank, and 2 matching cards of another rank.
        Ties broken based on the rank of the matching 3.'''

    def check_fourKind(hand):
        ''' Four of a kind. 4 matching cards of the same rank, and an unrelated side card.
        Ties broken based on the rank of the 4 cards.'''

    def check_straightFlush(hand):
        ''' Straight flush. A straight and a flush, i.e. 5 cards in sequence, all the same suit.
        Ties broken based on value of high card. An Ace-high straight flush is called a royal flush and is the highest possible hand without wild cards.
        (Some variants with wild cards make 5 of a kind possible; we won’t be using those variants.)'''
