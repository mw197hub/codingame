import sys
import math
import time

def formel1(a,b,c,d):
    return a**2+b**2+c**2+d**2
def formel2(b,c,d):
    summe=b+3*c+5*d
    return math.sqrt(summe)


n = 12345 #313
#n=9 #3 
#n=1000

abcList=[];sumList=[]
erg=0
ende = int(math.sqrt(n)+1)
anfangZeit = time.time()
anzahl=0
for b in range(0,ende):        
    for c in range(0,ende):
        if b+c>ende*2+10:
            break
        for d in range(0,ende):
            if b+c+d>ende*2+10:
                break       
            anzahl+=1  
            e=formel2(b,c,d)            
            if int(e) == e:  
                wertA=n-b**2-c**2-d**2
                if wertA >= 0: 
                    a= math.sqrt(wertA)
                    if a == int(a):          
                        wert=formel1(a,b,c,d)
                        if wert == n:                        
                            erg+=1
                            abcList.append([a,b,c,d,e])
                
print('{:5.3f}s'.format(time.time()-anfangZeit))
print(abcList,file=sys.stderr)
print(erg)
print(anzahl,file=sys.stderr)