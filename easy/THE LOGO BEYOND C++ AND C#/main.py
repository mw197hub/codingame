# https://www.codingame.com/training/easy/the-logo-beyond-c-and-c

import sys,math,copy

size,thickness=13,5
logoList=['+++', '++']

size,thickness=11,3
logoList=['++', '+++',' ++']

oben,unten,rechts,links=False,False,False,False
bildYX=[];bildLeer=[]
half=(size-thickness)/2
for j in range(len(logoList)):
    logo = logoList[j]    
    for y in range(size):
        zeile=""
        for i in range(len(logo)):        
            zeichen = logo[i]
            oben,unten,rechts,links=False,False,False,False
      #      oben = True if j == 0 else False
            try:
                if logoList[j-1][i] == " " or j-1 < 0:
                    oben = True
            except:
                oben = True
            
        #    unten = True if j == len(logoList)-1 else False
            try:
                if logoList[j+1][i] == " " or j+1 == len(logoList):
                    unten = True
            except:
                unten = True
            
            try:
                if logo[i+1] == " " or i+1 == len(logo):
                    rechts = True
            except:
                rechts=True
         #   rechts = True if i == 0  else False
            try:
                if logo[i-1] == " " or i-1 < 0:
                    links=True
            except:
                links=True
         #   links = True if i == len(logo)-1 else False
            for x in range(size):
                wert=" "
                if (y == half or y == half+thickness-1) and (x <= half or x >= half+thickness-1):
                    wert=zeichen
                if (x == half or x == half+thickness-1) and (y <= half or y >= half+thickness-1):        
                    wert=zeichen

                if (y == 0 ) and (x >= half and x <= half+thickness-1) and (oben):
                    wert=zeichen
                if (y == size-1) and (x >= half and x <= half+thickness-1) and (unten):
                    wert=zeichen

                if (x == 0) and (y >= half and y <= half+thickness-1) and (links):
                    wert=zeichen
                if (x == size-1) and (y >= half and y <= half+thickness-1) and (rechts):
                    wert=zeichen

                zeile+=wert
        print(zeile.rstrip())





