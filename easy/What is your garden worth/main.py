# https://www.codingame.com/ide/puzzle/what-is-your-garden-worth

import sys,math

offerList=[b'$12 = \xf0\x9f\x8d\x93\xf0\x9f\xa5\x92\xf0\x9f\x8c\xbf\xf0\x9f\x8c\xb9', b'$10 = \xf0\x9f\x8d\x83\xf0\x9f\x8d\x8d']
gardenList=[b'\xf0\x9f\x8c\xb1 #~', b'%+ @\xf0\x9f\x8d\x93', b'>{~\xf0\x9f\x8c\xb1', b'};-\xf0\x9f\xa5\x9c', b' ?!${']


summe=0
offerDict={}
for offer in offerList:
    oList=offer.split(b' ')
    #print(oList[1].decode())    
    offerDict[oList[0].decode()[1:]] = list(oList[2].decode()) #.split('')
print(offerDict,file=sys.stderr)

for garden in gardenList:
    zeile = garden.decode()
    for z in zeile:
        for wert,sym in offerDict.items():
            if z in sym:
                summe+=int(wert)
                
print('${:,}'.format(summe))
