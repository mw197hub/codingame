# https://www.codingame.com/ide/puzzle/the-optimal-urinal-problem

import sys,math




###
'''
anzahl=0;index=0;anz=0;posDict={}
for i in range(1,int((n+3)//2)):
    posDict.clear()
    pos = i;anz+=1;posDict[i]=[1,n]
    while True:

    
        if anz > anzahl:
            index=i;anzahl=anz
'''
mem_f = [0,1,1,2,2] # Memoization array
mem_f.extend([-1]*(1500001))

def f(n):
    '''
    Calculate the number of people that can use the toilet
    if the first and the last urinals are occupied
    '''
    global mem_f
    if mem_f[n]>-1:
        return mem_f[n]
    if n%2==1:
        mem_f[n] = 2*f((n+1)//2)-1
        return mem_f[n]
    else:
        half = n//2
        mem_f[n] = f(half)+f(half+1)-1
        return mem_f[n]

def start(n):

    max_gn = 0
    max_i = -1
    for i in range(1,(n+1)//2 + 1): # Since the problem is symmetric, just try the first half
        gn = f(i)+f(n+1-i)-1 # The core idea for this problem =)
        if gn > max_gn:
            max_gn = gn
            max_i = i
    return (max_gn, max_i)

n = 3 #1
n = 7
print('{} {}'.format(*start(n)))    