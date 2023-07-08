#https://www.codingame.com/ide/puzzle/nato-alphabets-odd-uncles

import sys,math

def setYear(yList,yearS):
    yTeil = yearS.split(",")
    yT1=[]
    for y in yTeil:
        yT1.append(y.strip())
    yList.append(yT1)
    #print(yT1,file=sys.stderr)


Y1908="Authority, Bills, Capture, Destroy, Englishmen, Fractious, Galloping, High, Invariably, Juggling, Knights, Loose, Managing, Never, Owners, Play, Queen, Remarks, Support, The, Unless, Vindictive, When, Xpeditiously, Your, Zigzag"
Y1917="Apples, Butter, Charlie, Duff, Edward, Freddy, George, Harry, Ink, Johnnie, King, London, Monkey, Nuts, Orange, Pudding, Queenie, Robert, Sugar, Tommy, Uncle, Vinegar, Willie, Xerxes, Yellow, Zebra"
Y1927="Amsterdam, Baltimore, Casablanca, Denmark, Edison, Florida, Gallipoli, Havana, Italia, Jerusalem, Kilogramme, Liverpool, Madagascar, New-York, Oslo, Paris, Quebec, Roma, Santiago, Tripoli, Uppsala, Valencia, Washington, Xanthippe, Yokohama, Zurich"
Y1956="Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu"

inputLine="Authority Bills Capture"

yList=[]
setYear(yList,Y1908)
setYear(yList,Y1917)
setYear(yList,Y1927)
setYear(yList,Y1956)
iList=inputLine.split(" ")
suchWert=-1
for i in range(len(yList)):
    treffer=0
    for il in iList:
        if il in yList[i]:
            treffer+=1
    print(treffer,file=sys.stderr)
    if treffer == len(iList):
        suchWert=i;break
print(suchWert,file=sys.stderr)
suchWert = 0 if suchWert == len(yList) -1 else suchWert +1
erg=""
suchList=yList[suchWert]
for il in iList:
    for s in suchList:
        if il[0] == s[0]:
            erg+=s+" "
            break
print(erg[:-1])
