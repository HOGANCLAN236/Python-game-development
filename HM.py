# Statement = input("Say a sentence: ").lower()

# Alphabet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
# AlphabetList = {}
# SpecialChar = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "|", "[", "]", "{", "}", ":", ";", "@", "'", "~", "#", ",", "<", ".", ">", "/", "?"]
# SpecialCharList = {}
# Digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# DigitsList = {}

# for i in Statement:
#   if i in Alphabet:
#     if i in AlphabetList:
#       AlphabetList[i] += 1
#     else:
#       AlphabetList[i] = 1

# print(AlphabetList)

# for i in Statement:
#   if i in SpecialChar:
#     if i in SpecialCharList:
#       SpecialCharList[i] += 1
#     else:
#       SpecialCharList[i] = 1

# print(SpecialCharList)

# for i in Statement:
#   if i in Digits:
#     if i in DigitsList:
#       DigitsList[i] += 1
#     else:
#       DigitsList[i] = 1

# print(DigitsList)

Statement = input("Say a sentence: ").lower()

Alphabets = 0
Digits = 0
Special = 0

for i in range(len(Statement)):
    if(Statement[i].isalpha()):
        Alphabets += 1
    elif(Statement[i].isdigit()):
        Digits += 1
    else:
        Special += 1
    
print("The count of alphabets are: ", Alphabets)
print("The count of digits are: " + str(Digits))
print("The count of special characters are: " + str(Special))




