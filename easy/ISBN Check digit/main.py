import sys
import math

def isbn11(isbn):
    erg=0
    for i in range(9):
        if not isbn[i] in ['0','1','2','3','4','5','6','7','8','9']:
            return False
        erg= erg + ( int(isbn[i]) * (10 - i))
    rest = (erg % 11)
    if not rest == 0:
        rest = 11 - rest
    if rest == 10:
        rest = "X"
    if isbn[9] == str(rest):
        return True
    return False

def isbn13(isbn):
    erg=0
    for i in range(12):
        if not isbn[i] in ['0','1','2','3','4','5','6','7','8','9']:
            return False
    for i in range(0,12,2):
        erg= erg + ( int(isbn[i])*1 + int(isbn[i + 1])*3)
    rest = (erg % 10)
    if not rest == 0:
        rest = 10 - rest
    if isbn[12] == str(rest):
        return True
    return False


isbnList=['0306406152', '013603599X', '1145185215X', '9780306406157', '9780306406154', '978043551907X']
isbnList=['0470371722', '9781119247792', '9780470124512', '11190495550', '1118105354', '9781118737637', '0387372350', '154875155X', '9781548751555', '978193981677']
isbnList=['0387372350']
isbnList=['9780133661750']

ergList=[]
for isbn in isbnList:
    if len(isbn) == 10:
        if not isbn11(isbn):
            ergList.append(isbn)
    elif len(isbn) == 13:
        if not isbn13(isbn):
            ergList.append(isbn)
    else:
        ergList.append(isbn)

print(str(len(ergList)) + " invalid:")
for isbn in ergList:
    print(isbn)