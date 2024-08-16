
Number = int(input("Choose a number between 1 and 9: "))

while Number != 1:
    if (Number % 2) == 0:
        Number = Number / 2
    else:
        Number = (Number * 3) + 1
    print(Number)
