import sys
import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

n=3

#ergList=[]
ergList = [['x' for i in range(n)]for j in range(n)]
#for i in range(n):
#    ergList.append(list('x' for j in range(n)))

y,x=n-1,n-1;m=0
moveDict={0:[0,-1],1:[-1,0],2:[0,1],3:[1,0]}
for i in range(n*n,0,-1):
    #print(i,file=sys.stderr)
    ergList[y][x] = '#' if is_prime(i) else ' '
        
    move = moveDict[m]    
    y1= y+ move[0];x1=x+move[1]
    if y1 < 0 or x1 < 0 or y1 == n or x1 == n or not ergList[y1][x1] == 'x':
        m+=1
        if m > 3:
            m = 0
        move = moveDict[m]
    y += move[0];x+=move[1]
    

for erg in ergList:
    print(*erg)