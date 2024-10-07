# https://www.codingame.com/ide/puzzle/a-bit-of-accounting---lettering

import sys,math,string
from itertools import permutations

invoiceList=[5];paymentList=[5]
invoiceList=[10, 12, 10, 14];paymentList=[10, 24, 12]
invoiceList=[500, 20, 127, 3,243];paymentList=[500, 373, 20]


###

abcList=[]
for i in string.ascii_uppercase:
    abcList.append(i)

for pay in paymentList:
    invList=[];inv=""
    if pay in invoiceList:
        invList.append(pay)
        invoiceList.remove(pay)
    else:
        fertig=False
        perm = permutations(invoiceList,2)
        for p in perm:
            if sum(p) == pay:                
                for j in p:
                    invoiceList.remove(j)
                    invList.append(j)
                fertig = True
                break
        if not fertig:
            perm = permutations(invoiceList,3)
            for p in perm:
                if sum(p) == pay:                
                    for j in p:
                        invoiceList.remove(j)
                        invList.append(j)
                    fertig = True
                    break
    for i in invList:
        inv=inv+" "+str(i)
    print("{} {} - {}".format(abcList.pop(0),pay,inv[1:]))
