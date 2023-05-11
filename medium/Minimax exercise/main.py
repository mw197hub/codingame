# https://www.codingame.com/ide/puzzle/minimax-exercise

import sys,math,time

MAX, MIN = 1000, -1000
 
# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta,maxDepth,ziffern,anzahl):
    anzahl[0]+=1
    # Terminating condition. i.e
    # leaf node is reached
    if depth == maxDepth:
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = MIN
 
        # Recur for left and right children
        for i in range(0, ziffern):
             
            val = minimax(depth + 1, nodeIndex * ziffern + i,
                          False, values, alpha, beta,maxDepth,ziffern,anzahl)
            best = max(best, val)
            alpha = max(alpha, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = MAX
 
        # Recur for left and
        # right children
        for i in range(0, ziffern):
          
            val = minimax(depth + 1, nodeIndex * ziffern + i,
                            True, values, alpha, beta,maxDepth,ziffern,anzahl)
            best = min(best, val)
            beta = min(beta, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best



#1
d,b=1,4
leafList=['2', '-1', '3', '0']
#2
#d,b=2,2
#leafList=['1', '2', '3', '4']
#4
#d,b=3,2
#leafList=['-1', '0', '2', '666', '-3', '-2', '666', '666']
#5
d,b=5,2
leafList=['-821', '-318', '46', '-870', '-595', '-56', '-817', '-170', '-464', '1', '-212', '67', '-83', '-233', '-263', '83', '-890', '-713', '-141', '-320', '-676', '93', '-794', '-175', '-322', '-481', '-916', '-761', '91', '37', '-464', '-194']


startTime=time.time()
values=[]
for leaf in leafList:
    values.append(int(leaf))

ziffern=b
maxDepth=d
anzahl=[0]
erg = minimax(0, 0, True, values, MIN, MAX,maxDepth,ziffern,anzahl)
print("{} {}".format(erg,anzahl[0]))



print("Laufzeit {}".format(time.time()-startTime),file=sys.stderr)