# https://www.codingame.com/training/easy/decode-the-message

import sys,math

p=35
c='abcdefghijklmnopqrstuvwxyz'  #ja

p=13484
c='abcdefghijklmnopqrstuvwxyz'  #qxs

p=2060735972420674
c='abcdefghijklmnopqrstuvwxyz !ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ergList=[]
print(len(c),file=sys.stderr)
runde=0
while p > len(c): 
    if runde == 0:   
        ergList.append(c[int(p%len(c))])        
    else:
        ergList.append(c[int(p%len(c)-1)])
    p = int(p / len(c))
    print(p,file=sys.stderr)
    runde+=1
ergList.append(c[p -1])

print("".join ([str(e) for e in ergList]))