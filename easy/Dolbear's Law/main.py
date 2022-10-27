import sys
import math
import statistics

iList=[8, 8, 6, 3, 2, 4, 8, 6, 9, 5, 2, 1, 5, 2, 8, 8, 3, 3, 6, 7, 2, 8, 1, 7, 4, 5, 4, 2, 3, 9]



n60List=[]
pos = 0
while pos < len(iList):
    n60 = 10 + (sum(iList[pos:pos+15]) - 40) / 7
    pos+=15
    n60List.append(n60) 
n60 = round(statistics.mean(n60List),1)
print(n60)

if n60 >= 5 and n60 <= 30:
    n8 = round(((sum(iList)/(len(iList)/2)) + 5),1)
    print(n8)