import Poker
import Hand

def main():
        #dealer
    
'''
    deck = Card.shuffled_deck()
    hand = []
    opp1 = []
    opp2 = []
    opp3 = []
    opp4 = []
    comm = []
    print('>> Card Generator v1 <<')
    while True:
        try:
            n = 3
        except ValueError:
            print('Invalid input, please enter a number!\n')
        else:
            if n < 1 or n >= 53:
                print('Please enter a number between 1-52!\n')
            else:
                break
    for i in range(n):
        hand.append(deck[i])
        opp1.append(deck[i+3])
        opp2.append(deck[i+6])
        opp3.append(deck[i+9])
        opp4.append(deck[i+12])
        comm.append(deck[i+15])
        #i =+ 6
    comm.append(deck[n+16])
    comm.append(deck[n+17])
'''
    
    #table
    print('Your hand is:')
    print(hand)
    print('Community Cards are:')
    print(comm)

    print(opp1)
    print(opp2)
    print(opp3)
    print(opp4)

    #Analysis
    print('Likelihood of winning is: ')
    print(Poker.check_hand(hand, comm))   
    
    #new hand
    input()
    main()

#main initiator
main()
