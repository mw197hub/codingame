import sys
import math
import string

sList = ['LOUISI', 'LOUISII', 'LOUISIII', 'LOUISIV', 'LOUISV', 'LOUISVI', 'LOUISVII', 'LOUISVIII', 'LOUISIX', 'LOUISX', 'LOUISXI', 'LOUISXII', 'LOUISXIII', 'LOUISXIV', 'LOUISXV', 'LOUISXVI']
n=16

sList = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN']
n=10

sList = ['ABCHZ', 'ABDAA']
n = 2

sList = ['A', 'AA']
n = 2

sList = ['JAMES', 'JENNIFER', 'JESS', 'JESSICA', 'JOHN', 'JOSEPH']
n=6

sList = ['MN', 'MO']
n = 2

#print(string.ascii_uppercase)
sortList = sorted(sList)
one = sortList[int(n/2 -1)]
two = sortList[int(n/2)]
print(one)
print(two)

erg = ""
anzahl = 0
gleich = True
for i in range(len(one)):
    anzahl = i
    if not one[i] == two[i]:
        gleich = False
        break

if len(one) == 1 or gleich or anzahl == len(one) -1:
    erg = one
else:
    nr = string.ascii_uppercase.index(one[anzahl])
    erg = one[:anzahl] + string.ascii_uppercase[nr +1]
    if erg == two:
        erg = one

print(erg)