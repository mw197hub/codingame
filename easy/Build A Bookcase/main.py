# https://www.codingame.com/ide/puzzle/build-a-bookcase

import sys,math

height, width, number_of_shelves = 8,13,3
#height, width, number_of_shelves = 3,3,2
#height, width, number_of_shelves = 10,6,5
#height, width, number_of_shelves = 11,15,4
height, width, number_of_shelves = 10,6,5


ebeneList=[height-1]
schritt = (height -1) // (number_of_shelves)
rest = (height -1) - (schritt * number_of_shelves)
for i in range(number_of_shelves-1):
    if i > number_of_shelves -1 -rest:
        a = i - number_of_shelves +1 +rest
        ebeneList.append(schritt*(i+1)+(a))
    else:
        ebeneList.append(schritt*(i+1))
for h in range(height):
    for w in range(width):
        if h == 0:
            if w == width //2 and not width == width//2 * 2 :
                print("^",end="")
            elif w < width // 2:
                print('/',end="")
            else:
                print("\\",end="")
        else:
            if w == 0 or w == width -1:
                print("|",end="")
            else:
                if h in ebeneList:
                    print("_",end="")
                else:
                    print(" ",end="")
    
    print("")