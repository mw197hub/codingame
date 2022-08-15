import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def pruefe(word,letters,p):
    lList = list(letters)
    for w in word:
        if w in lList:
            lList.remove(w)
        else:
            p = 0        
    return p

def points(word,abcDict):
    p = 0
    for b in word:
        p = p + abcDict[b]
    return p

abcDict = {'e':1,'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
wordDict = {}
wordDict = {'after': 8, 'repots': 8, 'poowers': 12, 'powers': 11, 'these': 8, 'time': 6, 'know': 11, 'from': 9, 'could': 8, 'people': 10}
letters = "tsropwe"

#n = int(input())
#for i in range(n):
#    w = input()
#    wordDict[w] = points(w,abcDict)
#letters = input()
print(wordDict,file=sys.stderr)
print(letters,file=sys.stderr)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

erg="";punkte=0
for word,p in wordDict.items():
    p = pruefe(word,letters,p)
    if p > 0 and p > punkte:
        erg = word; punkte = p

print(erg)