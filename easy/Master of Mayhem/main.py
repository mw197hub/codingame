import sys
import math

nameList = ['SPEEDO', 'TYPO']
mayhemList = ["Mayhem's hat is a FEDORA", "Mayhem's neckwear is a STRING OF PEARLS", 'Mayhem\'s word is "SNARK"']
cyborgList = ["SPEEDO's hat is a FEDORA", 'TYPO\'s catchphrase is "I am HUNTING for a SNARK"', "TYPO's companion is a MINIATURE DRAGON", "SPEEDO's neckwear is a STRING OF PEARLS", "SPEEDO's companion is a BEAVER", "TYPO's hat is a FEDORA", "TYPO's neckwear is a PENDANT"]




mayhemDict = {}
for mayhem in mayhemList:
    mayL = mayhem.split(" ")
    begriff = ""
    for i in range(4,len(mayL)):
        begriff = begriff + mayL[i] + " "
    begriff = begriff[:-1]
    if mayL[1] == "word":
        begriff = mayhem[mayhem.find("\"")+1:-1]
        mayL[1] = "catchphrase"
    mayhemDict[mayL[1]] = begriff
print(mayhemDict,file=sys.stderr)

nameList = ['MELLOW', 'YELLOW', 'FELLOW', 'BELLOW', 'JELLO', 'HELLO', 'CELLO']
nameList = ['MELLOW']
mayhemDict = {'hat': 'LAUREL WREATH', 'catchphrase': 'DANGER', 'neckwear': 'ASCOT', 'companion': 'AMORPHOUS BLOB'}
cyborgList = ["MELLOW's hat is a LAUREL WREATH", "YELLOW's hat is a LAUREL WREATH", "FELLOW's hat is a LAUREL WREATH", "BELLOW's hat is a LAUREL WREATH", "JELLO's hat is a LAUREL WREATH", "HELLO's hat is a LAMPSHADE", "CELLO's hat is a BOWLER", "MELLOW's neckwear is an ASCOT", "YELLOW's neckwear is an ASCOT", "FELLOW's neckwear is an ASCOT", "BELLOW's neckwear is a STETHOSCOPE", "JELLO's neckwear is an PENDANT", "HELLO's neckwear is an ASCOT", "CELLO's neckwear is an ASCOT", "MELLOW's companion is an AMORPHOUS BLOB", "YELLOW's companion is a FISH OUT OF WATER", "FELLOW's companion is an AMORPHOUS BLOB", "BELLOW's companion is an AMORPHOUS BLOB", "JELLO's companion is an AMORPHOUS BLOB", "HELLO's companion is an AMORPHOUS BLOB", "CELLO's companion is an AMORPHOUS BLOB", 'MELLOW\'s catchphrase is "CARE for a game of CATCH"', 'YELLOW\'s catchphrase is "FOLLOW me for DANGER"', 'CELLO\'s catchphrase is "STRANGER DANGER"', 'BELLOW\'s catchphrase is "DANGER is my MIDDLE name"', 'JELLO\'s catchphrase is "I LIVE for DANGER"', 'HELLO\'s catchphrase is "You are in DANGER of my WRATH"', 'FELLOW\'s catchphrase is "TIPTOE through the TULIPS"']
cyborgList = ["MELLOW's catchphrase is \"CARE for a game of CATCH\""]

for begriff in cyborgList:
    begriffList = begriff.split(" ")
    name = begriffList[0]
    name = name[:-2]
    if begriffList[1] in mayhemDict:
        if begriffList[1] == "catchphrase":
            if begriff.find(mayhemDict["catchphrase"]) == -1:
                nameList.remove(name)
        else:
            begriff = ""
            for i in range(4,len(begriffList)):
                begriff = begriff + begriffList[i] + " "
            begriff = begriff[:-1]
            if not begriff == mayhemDict[begriffList[1]] and name in nameList:
                nameList.remove(name)


print(nameList,file=sys.stderr)

if len(nameList) == 1:
    print(nameList[0])
elif len(nameList) == 0:
    print("MISSING")
else:
    print("INDETERMINATE")
