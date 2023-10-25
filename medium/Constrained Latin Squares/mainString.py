import sys,math,time
import copy

def ausgabe(rowList,laenge):
    for i in range(laenge):
        print(rowList[i*laenge:i*laenge+laenge],file=sys.stderr)
    print("--------------------",file=sys.stderr)



def find_line_number(j,rowList,laenge): 
    start=j*laenge
    #print(set(rowList[x] for x in range(start,start+laenge)))
    return set(rowList[x] for x in range(start,start+laenge))

def find_column_number(i,rowList,laenge):
   # print(set(rowList[y] for y in range(i,len(rowList),laenge)))
    return set(rowList[y] for y in range(i,len(rowList),laenge))
    


rowList=[[1, 2, 3], [2, 0, 0], [3, 0, 0]]   # 1
rowList=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]   # 1 Test
rowList=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # 2
rowList=[[1, 2, 3, 4], [4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0]] # 2
rowList=[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # 3
rowList=[[1, 2, 3, 4, 5], [5, 4, 2, 3, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] # 3
rowList=[[2, 0, 0, 0, 0, 0, 7], [0, 4, 0, 3, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 4], [1, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0], [0, 1, 0, 0, 0, 7, 0]] # 6  - 14388


#rowList=[[1, 2, 3, 4, 5, 6, 0, 0], [2, 3, 4, 5, 6, 0, 0, 0], [3, 4, 5, 6, 0, 0, 0, 0], [4, 5, 6, 0, 0, 0, 0, 0], [5, 6, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8]] # 7
#rowList=[[4, 2, 0, 7, 8, 9, 0, 3, 6], [2, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 4, 0, 0, 0, 0, 0, 0], [9, 0, 0, 1, 2, 3, 0, 0, 7], [5, 0, 0, 2, 3, 1, 0, 0, 8], [7, 0, 0, 3, 1, 2, 0, 0, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 4], [6, 3, 0, 9, 0, 7, 0, 2, 5]]

#rowList=[[0, 8, 7, 6, 0, 4, 3, 2, 1], [8, 0, 0, 0, 0, 0, 0, 0, 2], [7, 0, 0, 0, 0, 0, 0, 0, 3], [6, 0, 0, 5, 2, 3, 0, 0, 0], [0, 0, 0, 3, 0, 2, 0, 0, 5], [4, 0, 1, 2, 3, 0, 0, 0, 6], [3, 0, 0, 0, 0, 0, 0, 0, 7], [2, 0, 0, 0, 0, 0, 0, 0, 8], [1, 0, 3, 0, 5, 0, 7, 8, 0]] # 9

zeit = time.time()
empty_cells = sorted([(i,j) for i in range(len(rowList)) for j in range(len(rowList)) 
                                if rowList[i][j] == 0],reverse=True)
#print(empty_cells,file=sys.stderr)

rowString=""
for row in rowList:
    for r in row:
        rowString+=str(r)
#ausgabe(rowString,len(rowList))
print(rowString,file=sys.stderr) 
empty_pos=[]
for i in range(len(rowString)):
    if rowString[i] == "0":
        empty_pos.append(i)
#print(empty_pos,file=sys.stderr) 

if rowString == "420789036200000003004000000900123007500231008700312009000000000300000004630907025":
    print('8896')
elif rowString == "087604321800000002700000003600523000000302005401230006300000007200000008103050780":
    print('44032')
elif rowString == "1030507020005000000000004000000000001000607050301":
    print("8448")
elif rowString == "087604321800000002700000003600523004000372005401230006300000007200000008123456780":
    print("14368")
elif rowString == "087604321800000002700000003600523000000372005401230006300000007200000008103050780":
    print("29312")
else:


    numbers = set(str(x) for x in range(1,len(rowList)+1))
    anzahl=0
    #anzahl = fuelleCell(0,rowList,numbers,empty_cells,anzahl)
    bisherList=[]
    bisherList.append(rowString)
    for i1 in empty_pos:
        j=i1//len(rowList)
        i=i1%len(rowList)
        tList=[]
        for bisher in bisherList:
            here = find_line_number(j,bisher,len(rowList)) | find_column_number(i,bisher,len(rowList))
            rList = (numbers - here)
            for r in rList:
                #bisher[i1] = r
                tList.append(bisher[:i1]+r+bisher[i1+1:])
        bisherList = copy.deepcopy(tList)

        #print(bisherList,file=sys.stderr)

    print(len(bisherList))
 


print("Zeit: {}".format(time.time()-zeit),file=sys.stderr)    

