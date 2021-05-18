import sys
import math
import time

def sucheAnfang(word,textNew):
    allList = []
    posList = []
    keinTreffer = False
    maxWert = 9999
    for w in word:
        anzahl = 0
        posList.clear()
        for t in textNew:        
            if t == w:
                posList.append(anzahl)
            anzahl += 1
        if len(posList) == 0:
            keinTreffer = True
        if len(posList) > 0 and posList[len(posList)-1] < maxWert:
            maxWert = posList[len(posList)-1]
        allList.append(posList[:])
    return keinTreffer,allList,maxWert



text = "some wacky runes a tourist found"
text = "To be or not to be that is the question Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune Or to take arms against a sea of troubles And by opposing end them To die to sleep No more and by a sleep to say we end The heartache and the thousand natural shocks That flesh is heir to"
#ThertisnoblerinthemindtosuffeRtheslingsandarrowsofoutrageoUsfortuneortotakearmsagainstaSeaoftroublesandbyopposingendT
#text = "Blessed is he, who in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper - and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy my brothers."
#ErskeeperandthefinderofLostchildrenandiwillstrIkedownupontheewithgreaTvengeanceandfuriousangE
#text = "abcdefghijklmnopqrstuvwxyz h!@#$%^&*aealap aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

#  abcdefghijklmnopqrstuvwxyz h!@#$%^&* '"-=_+`~;:()[]{}<>/\?,.aealap aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#  HaEaLaP

wordList = ['secret', 'hidden', 'invisible', 'message']
wordList = ['aliens', 'conspiracy', 'theory', 'resistance', 'trust', 'power', 'corrupt']
#wordList = ['secret', 'hidden', 'invisible', 'message', 'obfuscate', 'clandestine', 'aliens', 'conspiracy', 'theory', 'resistance', 'power', 'corrupt', 'iron', 'rule', 'pestilence', 'plague', 'waste', 'trust', 'elite', 'illuminati', 'privileged', 'birth', 'senate', 'dictator', 'caesar', 'king', 'citizen', 'sheep']
#wordList = ['aaaaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaaaac', 'aaaaaaaaaaaaaaaaad', 'aaaaaaaaaaaaaaaaaf', 'aaaaaaaaaaaaaaaaag', 'aaaaaaaaaaaaaaaaai', 'aaaaaaaaaaaaaaaaak', 'aaaaaaaaaaaaaaaaam', 'aaaaaaaaaaaaaaaaan', 'aaaaaaaaaaaaaaaaaq', 'aaaaaaaaaaaaaaaaar', 'aaaaaaaaaaaaaaaaas', 'aaaaaaaaaaaaaaaaat', 'aaaaaaaaaaaaaaaaau', 'aaaaaaaaaaaaaaaaav', 'aaaaaaaaaaaaaaaaaw', 'aaaaaaaaaaaaaaaaax', 'aaaaaaaaaaaaaaaaay', 'aaaaaaaaaaaaaaaaaz', 'help']


startTime = time.time()
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wordList.sort(key=lambda x:len(x))
textNew = ""
for t in text:
    if t.lower() in abc:
        textNew += t.lower()
#print(len(textNew),file=sys.stderr)
ergebnis = ""
ergList = []
diff = 0
while wordList:
    word = wordList.pop()
    print(word,file=sys.stderr)
    ergebnis = ""
    treffer = True
    keinTreffer,startList, maxWert = sucheAnfang(word,textNew)
    if not keinTreffer:
        #print(startList,file=sys.stderr)
        print(maxWert,file=sys.stderr)
        firstList = startList[0]
        secondList = startList[1]
        for first in firstList: 
            if first > maxWert:
                treffer = False
                break           
            for second in secondList:
                treffer = False
                if first < second:
                    ergList.clear()
                    ergList.append(first)
                    ergList.append(second)
                    diff = second - first
                    pos = second                    
                    for i in range(2,len(word)): 
                        treffer = False                       
                        for rest in startList[i]:
                            if rest == pos + diff:
                                ergList.append(rest)
                                treffer = True
                                pos = rest
                                break
                        if not treffer:
                            break
                if treffer:
                    break
            if treffer:
                break
        if treffer:
            break
 
print(ergList,file=sys.stderr)

textNew2 = ""
for i in range(len(textNew)):
    if i in ergList:
        textNew2 += textNew[i:i+1].upper()
    else:
        textNew2 += textNew[i:i+1]
ergebnis = textNew2[ergList[0]:ergList[len(ergList)-1]+1]
print(ergebnis)

print('{:5.3f}s'.format(time.time()-startTime))