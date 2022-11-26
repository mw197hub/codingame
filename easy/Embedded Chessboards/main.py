import sys,math

def werte(r,c):
     a=0
     if r < 0 or c < 0:
          return 0
     nR=int(r/2) 
     nC=int(c/2) 
     a = (nR+1)*(nC+1)
     return a


rList=['8 8 0', '9 8 1', '8 10 0', '10 9 0', '10 11 1']

for r in rList:
     anz=0
     row,col,white = [int(j) for j in r.split()]     
     if white == 1:
          anz += werte(row -8,col -8)
          anz += werte(row -9,col -9)
     else:
          anz += werte(row -8,col -9)
          anz += werte(row -9,col -8)
     print(anz)
