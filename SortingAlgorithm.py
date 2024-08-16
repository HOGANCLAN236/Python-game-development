import random
import time

List = []

hasDone = False

for i in range(100000):
    Num = random.randint(0, 100000000000)
    List.append(Num)


def bubbleSort():
    swapped = False
    for i in range(len(List)-1,0,-1):
        for j in range(i):
            if List[j]>List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return List


hasDone = True
if(hasDone == True):
    bubbleSort()

print(List)
