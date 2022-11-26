import math,sys


s='HAYEKXQIUZMVLTJYRNTZTN'
#s='ABCB'
#s='SCTAYLZPYPZNCFGHFHEUWJUVRKFMZMICSMDZOEKNIUFYAGPAUNNCCHAVYHCZNKIEZARASZWXFBJNFIXUQZTFWEDDANXOIXSNVNNPNNVNSXIOXNADDEWFTZQUXIFNJBFXWZSARAZEIKN'


for i in range(len(s)-2,-1,-1):
    l = len(s)-1 - i
    t=''.join(reversed(s[i-l:i]))
    if s[i+1:] == t:
        print(i+1-(len(s)-i))
        break
#print(s.count('T'))
#print(s.find('T'))
#print(s.index('T',17))