# https://www.codingame.com/ide/puzzle/agent-x-mission-1-the-caesar-cipher

import sys,math

def umsetzen(ciphertext,i,abcDict,numDict):
    erg=""
    for buch in ciphertext:
        num = numDict[buch]
        num += i
        if num > 126:
            num -= 95
        neu = abcDict[num]
        erg+=neu
    return erg



ciphertext="Whvw/#whvw/#khoor$";word="test"


abcDict={}
numDict={}
for i in range(32,127,1):
    abcDict[i] = chr(i)
    numDict[chr(i)] = i
#print(abcDict,file=sys.stderr)

diff=0
erg=""

for i in range(95):
    tWord=umsetzen(ciphertext,i,abcDict,numDict)

    mdecode = tWord
    for sc in [',','.','!',':', '?',';']:
        mdecode = mdecode.replace(sc, ' ')
    words = mdecode.split()

    if word in words:
        diff = i
        erg=tWord
        break

print(95-diff)
print(erg)
