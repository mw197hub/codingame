# https://www.codingame.com/ide/puzzle/roller-coaster

import sys,math,time,copy
from functools import lru_cache as memoize

l=3;c=3;pList=[3, 1, 1, 2]    #  1 = 7
#l=5;c=3;pList=[2, 3, 5, 3]    #  2 = 15
#l=10000;c=10;pList=[100, 200, 300, 400, 500]  # 4  = 15000
l=10000000;c=9000000;pList=[]  # 6 = 89744892565569
#l=100000;c=500000;pList=[]  # 5 = 4999975000
#l=3;c=10;pList=[3, 1, 1, 2]
#l=7;c=20;pList=[3, 5, 1, 2]

datei = open('C:\\Users\\marku\\Python\\codingame\\hard\\Roller Coaster\\input6.txt',"r")
for ein in datei:
    pList.append(int(ein))
datei.close()


# neuer Versuch
start=time.time()
posDict={};multiTrue=True
erg=0
pos=0;zaehler=0;wert=0;akt=0
if sum(pList)<=l:
    erg=sum(pList)*c
else:
    while True:
        akt=pList[pos]
        
        if wert+akt < l:
            wert+=akt
        else:
            if wert+akt == l:
                wert+=akt
                erg+=wert
                wert=0
            else:
                erg+=wert
                wert=akt
            zaehler+=1      
            if zaehler >= c:
                break
            
            if pos in posDict and multiTrue:
                z,e=posDict[pos]
                if pos == 0:
                    mehrfach=c//zaehler
                    erg=sum(pList)*(mehrfach)
                    zaehler=(mehrfach*(zaehler))

                else:                    
                    diffZ=zaehler-z
                    diffE=erg-e
                    restZ=c-zaehler
                    mehrfach=restZ//diffZ
                    erg+=mehrfach*diffE
                    zaehler+=mehrfach*diffZ
                multiTrue=False           
            posDict[pos] = (zaehler,erg)                      
            #print("{}    {} # {}".format(pos,zaehler,erg),file=sys.stderr)
            if zaehler >= c:
                break
        pos=pos+1 if pos < len(pList)-1 else 0

print(erg)
#print("Abweichung: {}".format(4999975000-erg))  # 5

print("Zeit 1: {}".format(time.time()-start),file=sys.stderr)

##########################################################
# loesung geklaut


L, rides, N = map(int, "10000000 9000000 1000".split())
groups  = copy.deepcopy(pList)
start=time.time()
totalpeople = sum(groups)
# Let's handle the case when the queue is less than
# available rides.
if totalpeople <= L:
    print(totalpeople * rides)
else:
    # Let's precalculate how much we earn each ride
    # and where will the queue move after the ride.
    jumps = []
    for i, group in enumerate(groups):
        revenue, counter = 0, i
        while revenue + groups[counter] <= L:
            revenue  += groups[counter]
            counter   = (counter + 1) % N
        jumps.append((counter, revenue))
    # Now all that's left is iterate through rides
    # and calculate the sum.
    total = queue = 0
    while rides:
        counter, revenue = jumps[queue]
        total += revenue
        queue  = counter % N
        rides -= 1
    print(total)

print("Zeit 2: {}".format(time.time()-start),file=sys.stderr)

######

slots, rides, groups_num = map(int, "10000000 9000000 1000".split())
groups = copy.deepcopy(pList)
start = time.time()
everyone = sum(groups)



@memoize(None)
def ride(group):
    ride_size = 0
    while (ride_size + groups[group] <= slots
        and ride_size + groups[group] <= everyone):
        ride_size += groups[group]
        group = (group+1) % len(groups)
    return ride_size, group

group = 0
dirhams = 0
for _ in range(rides):
    earning, group = ride(group)
    dirhams += earning

print(dirhams)

print("Zeit 3: {}".format(time.time()-start),file=sys.stderr)

#####################################

l, c, n = map(int, "10000000 9000000 1000".split())
#l, c, n = map(int, "7 20 4".split())
p = copy.deepcopy(pList)

start = time.time()
money = [0] * n
nextp = [0] * n

for i in range(n):
    pos = i
    cnt = 0
    cur = l
    while cnt < n and p[pos] <= cur:
        cur -= p[pos]
        money[i] += p[pos]
        cnt += 1
        pos += 1
        if pos == n:
            pos = 0
    nextp[i] = pos

ans = 0
pos = 0
for i in range(c):
    ans += money[pos]
    pos = nextp[pos]

print(ans)

print("Zeit 4: {}".format(time.time()-start),file=sys.stderr)




# zu langsam
'''
start=time.time()
laeList=len(pList)
erg=0;rest=0;wert=0
for i in range(c):
    k=0
    while wert < l:        
        akt=pList.pop(0)
        pList.append(akt)
        wert+=akt
        k+=1
        if k == laeList:
            break
    if wert == l or k == laeList:
        akt=0
    else:
        wert-=akt
    erg+=wert
    wert=akt
print(erg)

print("Zeit: {}".format(time.time()-start),file=sys.stderr)

'''