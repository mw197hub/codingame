# https://www.codingame.com/ide/puzzle/histogram

import sys,math,string

s='A'
s='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
s='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'


abcDict={}

abc = string.ascii_uppercase
for a in abc:
    abcDict[a]=0
#print(abcDict,file=sys.stderr)
anzahl=0
for ab in s:
    if ab.upper() in abcDict:
        anzahl+=1
        abcDict[ab.upper()] += 1
vorher=0
for abc,wert in abcDict.items():
    p = (wert / anzahl * 100) 
    p = round(p,2)
    
    if round(p) > 0 or round(vorher) > 0:
        if round(p+0.01) > 0 and round(vorher+0.01) > 0:
            einf=""
            for i in range(int(max(round(p+0.01),round(vorher+0.01)))):
                if i == round(p+0.01) or i == round(vorher+0.01):
                    einf+="+"
                else:
                    einf+='-'
            print("  +{}+".format(einf))
        else:
            if vorher > p:
                print("  +{}+".format(round(vorher+0.01)*'-'))
            else:
                print("  +{}+".format(round(p+0.01)*'-'))
    else:
        print("  +")
    if round(p) > 0:        
        print("{} |{}|{:.2f}%".format(abc,round(p+0.01)*" ",p))
    else:
        print("{} |{:.2f}%".format(abc,p))
    vorher=round(p+0.01)

if vorher > 0:
    print("  +{}+".format(round(vorher+0.01)*'-'))
else:
    print("  +")

