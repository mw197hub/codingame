import sys
import math

def auswahl(wert,zaehler):
    erg = ""
    wertList = wert.split("|")
    i = zaehler
    if zaehler >= len(wertList):
        i = zaehler % len(wertList) 
    erg = wertList[i]
    return erg

def teil(start,zaehler,newLine):
    line = newLine[start:]
    ab = line.find("(")
    bis = line.find(")") +1
    print(line[:ab],end="")
    erg = auswahl(line[ab+1:bis-1],zaehler)
    if "#" in erg:
        ergL = erg.split("#")
        for e in ergL:
            print(e)
    else:
        print(erg,end="")
    zaehler += 1
    start = start + bis
    if "(" in (line[bis:]):        
        start,zaehler = teil(start,zaehler,newLine)
    return start,zaehler

zaehler = 0
lineList= ['This is the (first|second|third) choice.', 'This is the (first|second|third) choice.', 'This is the (first|second|third) choice.']
lineList = ['(Hello|Hi|Bonjour|Salut|Hey) (les amis|coders|bande de @$%*),', '', 'I keep getting an error( 492|) in the notification area.', 'Are you aware of that?', '', '(Bye|Ciao|Fsck off|Best regards),', 'Your Name Here']
lineList = ['(No choice)', '(Empty choice|)', 'Lotsa (1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100) choices', 'Does it (wrap|unwrap)?', '(Multi', 'line|Multi', 'line)']
#lineList = ['(You must|You need to|You have to|You should) (take advantage of|make the most of|benefit from|take full advantage of) (all the|all of the|each of the|every one of the) software advancements that (happen to be|are actually|are|are generally) (a successful|an effective|an excellent|a prosperous) (Internet marketer|Online marketer|Internet entrepreneur|Affiliate marketer). (If your|In case your|Should your|When your) work (begins to|starts to|actually starts to) suffer, (the competition|your competition|competition|your competitors) could (leave you|make you|create) (in the|within the|inside the|from the) dust. Show (that you are|that you will be|that you are currently|you are) always (on the|around the|in the|about the) (cutting edge|innovative|leading edge|really advanced), (and they will|and they can) (learn to|learn how to|figure out how to|discover how to) trust (you and your|both you and your|you and the|your) products.']
lineList = ['(Multi', 'line|Multi', 'line)']

zusammen = False
newList = []
newLine = ""
for line in lineList:
    if zusammen:
        newLine = newLine + "#" + line
        if ")" in line:
            zusammen = False
            newList.append(newLine)
    else:
        if "(" in line and not ")" in line:
            zusammen = True
            newLine = line
        else:
            newList.append(line)


for line in newList:
    if "(" in line:    
        start = 0    
        start,zaehler = teil(start,zaehler,line)
        print(line[start:],end="")
        print("")
    else:
        print(line)