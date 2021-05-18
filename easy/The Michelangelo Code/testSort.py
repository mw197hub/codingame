import sys

wordList = ['secret', 'hidden', 'invisible', 'message', 'obfuscate', 'clandestine', 'aliens', 'conspiracy', 'theory', 'resistance', 'power', 'corrupt', 'iron', 'rule', 'pestilence', 'plague', 'waste', 'trust', 'elite', 'illuminati', 'privileged', 'birth', 'senate', 'dictator', 'caesar', 'king', 'citizen', 'sheep']

#print(wordList)
#wordList.sort(key=len,reverse=False)
#print(wordList)

text = "ErskeeperandthefinderofLostchildrenandiwillstrIkedownupontheewithgreaTvengeanceandfuriousangE"
ergebnis = ""
anzahl = 0
schritt = 0
for t in text:
    if t.isupper():
        ergebnis += t
        if schritt == 0:
            schritt = anzahl
    anzahl += 1
print(ergebnis)
print(str(schritt))