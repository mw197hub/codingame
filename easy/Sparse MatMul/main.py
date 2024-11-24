# https://www.codingame.com/ide/puzzle/sparse-matmul


#aList=[];bList=[]
#m, n, p = [int(i) for i in input().split()]
#count_a, count_b = [int(i) for i in input().split()]
#for i in range(count_a):
#    inputs = input().split()
#    row = int(inputs[0])
#    column = int(inputs[1])
#    value = float(inputs[2])
#    aList.append([row,column,value])
#for i in range(count_b):
#    inputs = input().split()
#    row = int(inputs[0])
#    column = int(inputs[1])
#    value = float(inputs[2])
#    bList.append([row,column,value])
#print("m={};n={};p={}".format(m,n,p),file=sys.stderr)
#print("aList={};bList={}".format(aList,bList),file=sys.stderr)

import math,sys

m=4;n=3;p=5
aList=[[1, 0, 1.0], [1, 1, 2.0], [1, 2, 3.0]];bList=[[0, 3, 5.0], [2, 3, 1.0]]


####
