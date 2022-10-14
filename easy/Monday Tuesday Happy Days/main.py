import sys
import math

def tagNummer(monat,tag,monDict):
    tagNr=0
    for mon in range(12):
        if mon == monat:
            break
        tagNr+=monDict[mon]
    return tagNr+tag

monNr={'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'Jun':5, 'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
monDict={0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
dayDict={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday',6:'Sunday'}


leap_year=1
start=['Saturday', 'Feb', '21']
ende=['Mar', '1']

leap_year=0
start=['Friday', 'Sep', '13']
ende=['Jan', '2']

leap_year=0
start=['Monday', 'Jan', '3']
ende=['Jan', '2']

if leap_year == 1:
    monDict[1] = 29

startTag=tagNummer(monNr[start[1]],int(start[2]),monDict)
endeTag=tagNummer(monNr[ende[0]],int(ende[1]),monDict)

startNr=0
for nr,day in dayDict.items():
    if start[0] == day:
        startNr=nr

addDays=endeTag-startTag

rest=addDays%7
endeNr=(rest+startNr)%7
print(dayDict[endeNr])