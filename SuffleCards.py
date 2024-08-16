# NEXT HM: use loop and random for index and then append to different list and then pick 13 random and add to e.g hearts list 
import random 

CardsMax = 40

Cards = []

Hearts = []
Spades = []
Diamonds = []
Clubs = []

OtherMade = ["King", "Queen", "Jack"]
Other = []

ShieldList = []

for i in range(CardsMax):
    Card = random.randint(1, CardsMax)
    Num = random.randint(1, 10)

while len(ShieldList) < 40:
    Number = random.randint(1, 10)
    Shield = random.randint(1, 4)

    if Shield == 1 and len(Hearts) < 10 and Number not in Hearts:
        Hearts.append(Number)
        ShieldList.append(Number)
    else:
        pass
    if Shield == 2 and len(Spades) < 10 and Number not in Spades:
        Spades.append(Number)
        ShieldList.append(Number)
    else:
        pass
    if Shield == 3 and len(Diamonds) < 10 and Number not in Diamonds:
        Diamonds.append(Number)
        ShieldList.append(Number)
    else:
        pass
    if Shield == 4 and len(Clubs) < 10 and Number not in Clubs:
        Clubs.append(Number)
        ShieldList.append(Number)
    else:
        pass

while len(Other) < 12:
    CardNum = random.randint(0, 2)
    CardToAdd = OtherMade[CardNum]
    Shield = random.randint(1, 4)
    if Shield == 1 and len(Hearts) < 13 and CardToAdd not in Hearts:
        Hearts.append(CardToAdd)
        Other.append(CardToAdd)
    else:
        pass
    if Shield == 2 and len(Spades) < 13 and CardToAdd not in Spades:
        Spades.append(CardToAdd)
        Other.append(CardToAdd)
    else:
        pass
    if Shield == 3 and len(Diamonds) < 13 and CardToAdd not in Diamonds:
        Diamonds.append(CardToAdd)
        Other.append(CardToAdd)
    else:
        pass
    if Shield == 4 and len(Clubs) < 13 and CardToAdd not in Clubs:
        Clubs.append(CardToAdd)
        Other.append(CardToAdd)
    else:
        pass
    
random.shuffle(Hearts)
random.shuffle(Diamonds)
random.shuffle(Spades)
random.shuffle(Clubs)
Cards.append(Hearts)
Cards.append(Diamonds)
Cards.append(Spades)
Cards.append(Clubs)
print(Cards)
print("\n")
print(Hearts)
print("\n")
print(Diamonds)
print("\n")
print(Spades)
print("\n")
print(Clubs)

