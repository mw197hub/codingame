import sys
import math
import copy

n=1; deckList = ['AS', 'AH', 'AD', 'AC']
n=1; deckList = ['2S', '5D', 'QH', '3S', '4S', 'JH', 'JD', '5S', 'KH']
n=10;deckList = ['KS', 'KC', '4S', '5D', '7H', 'KH', 'AH', '9D', 'QH', '8S', '5C', 'JH', 'QS', '3S', 'AS', 'KD', '6D', '5H', '5S', 'JS']

deck1 = []
deck2 = []
ergList = []
erg = ""
split = int(len(deckList) / 2)
if len(deckList) % 2:
    split += 1

for i in range(n):
    deck1.clear();deck2.clear();ergList.clear()
    for j in range(len(deckList)):
        if j < split:
            deck1.append(deckList[j])
        else:
            deck2.append(deckList[j])
    one = True
    for j in range(len(deckList)):
        if one:
            ergList.append(deck1.pop(0));one=False
        else:
            ergList.append(deck2.pop(0));one=True
        
    deckList.clear();deckList = copy.deepcopy(ergList)

for i in range(len(ergList)):
    erg = erg + ergList[i] + " "
print(erg[:-1])