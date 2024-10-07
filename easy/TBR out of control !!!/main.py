# https://www.codingame.com/ide/puzzle/tbr-out-of-control

import sys,math,string

#1
newList=['A court of thorns and roses', 'Notre-Dame de Paris'];shelfList=['Powerless 9', 'The scarlet letter 8', 'Babbel None', 'Yellowface 4', 'Divine Rivals 5']

#5
newList=['A court of thorns and roses', 'Heartless', 'Notre-Dame de Paris', '1984'];shelfList=['Powerless 9', 'The scarlet letter 8', 'Babbel 6', 'Holly 6', 'Forth Wing 7', 'Moby-dick 3', 'Divine Rivals 6', 'Hunger games None', 'The villa 2', 'Ninth House 7']

#7
newList=['A court of thorns and roses', 'Powerless', 'Notre-Dame de Paris', '1984'];shelfList=['Powerless 9', 'The scarlet letter 8', 'Babbel None', 'Holly 6', 'Forth Wing None', 'Moby-dick None', 'Divine Rivals None', 'Hunger games None', 'The villa None', 'Ninth House 7']


#####
fehler='Your TBR is out of control Clara!'

ausgabeList=[]
bewertungDict={}
for new in newList:
    ausgabeList.append(new)
for book in shelfList:
    bList = book.split(' ')
    name = ''
    for i in range(len(bList)-1):
        name+=bList[i]+" "
    name=name[:-1]
    if bList[-1] == 'None':
        if name not in ausgabeList:
            ausgabeList.append(name)
    else:
        if bList[-1] in bewertungDict:
            bisher=bewertungDict[bList[-1]]
            bisher.append(name)
        else:
            bewertungDict[bList[-1]] = [name]

first=True
for wertung,bList in sorted(bewertungDict.items(),reverse=True):
    if first:
        first=False
        for name in bList:
            if name not in ausgabeList:
                ausgabeList.append(name)
                first = False
    else:
        if len(ausgabeList) + len(bList) <= len(shelfList):
            for name in bList:
                if name not in ausgabeList:
                    ausgabeList.append(name)
        else:
            break

if len(ausgabeList) > len(shelfList):
    print(fehler)
   # print(sorted(ausgabeList),file=sys.stderr)
else:
    for ausgabe in sorted(ausgabeList):
        print(ausgabe)





