import sys,math


grid=[[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2]]
size=9
empty_cells = sorted([(i,j) for i in range(size) for j in range(size) if grid[i][j] == 0],reverse=True)
print(empty_cells,file=sys.stderr)


print("".join([str(grid[y][x]) for y in range(size) for x in range(size)]))
for y in range(size):
    print("".join([str(grid[y][x]) for x in range(size)]))

line = set(grid[0][x] for x in range(size))
print(line)

testDict={'a':0,'b':1}
testList=['a','c','a']
for t in testList:
    testDict[t] = testDict[t] + 1 if t in testDict else 1
print(testDict)
test1Set=set('1')
test2Set=set('3')
test2Set.add('1')
print(test1Set & test2Set)
print(test1Set | test2Set)

test1List=[0,1,2]
test2List=[2,3]
print(test1List + test2List)

sortDict={'a':[0],'b':[1,2,3],'c':[]}
for e in sorted(sortDict.items(), key=lambda item: len(item[1]),reverse=False):
    print(e)


class test1:
    anzahl = 0   # klassenvariable
    def __init__(self,id):
        self.t1 = 0; self.id = id;test1.anzahl+=1    
    def __str__(self) -> str:
        return ("Ausgabe: %2d %2d " % (self.t1,self.id))
    @classmethod
    def m1(self,a,b):
        return a+b

tClass = test1(0)
tCl2=test1(3)
print(tClass)
#print(tClass.m1())
print(test1.anzahl)
#print(test1.m1(1,2))




#def product(a,b):
#    print(a+b)
#def produk(a,b,c):
#    print(a+b+c)
#product(1,1,9)             # bringt einen fehler

print("########## code golf ###############")
print(["A","B"][True&True&False])    #  |  or   & and
print(["falsch","wahr"][1<2<3])
print(['much','code','wow'][1])

X,Y=2,3
for a in range(X*Y):print(a//X,a%X)

#  i=input;a,b,c=i(),i(),i()
aList=[1,2,3]
*a,b=aList
print("{} # {}".format(a,b))

print("1234".zfill(7))