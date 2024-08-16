import random

Suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = [(suit, rank) for suit in Suits for rank in Ranks]

#Shuffling

random.shuffle(deck)

# for card in deck:
#     print(card[1], "of", card[0])

for i in range(5):
    print(deck[i][1], "of", deck[i][0])
