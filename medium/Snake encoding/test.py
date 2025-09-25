#
def affiche(liste):
    for i in range(len(liste)):
        lig=""
        for j in range(len(liste)):
            lig+=liste[j][i]
        print(lig)

def Encodage(liste):
    lres=[]
    for i in range(len(liste)):
        lres.append([])
    for i in range(len(liste)):
        if(i%2==0):
            lres[i]+=liste[i][1:]
            if i==0:
                if len(liste)%2==0:
                    lres[i].append(liste[len(liste)-1][len(liste)-1])
                else:
                    lres[i].append(liste[len(liste)-1][0])
            else:
                lres[i].append(liste[i-1][len(liste)-1])
        else:
            lres[i]+=liste[i-1][0]
            lres[i]+=(liste[i][:len(liste)-1])
    return lres




N=7;X=5
lineList=['I_LOVE_', 'TESTING', 'AMAZING', 'ENCODES', 'NOTYOU?', 'NUM83R5', 'NICE:)!']
#N=3;X=5
#lineList=['ABC', 'DEF', 'GHI']



l=[]


for i in range(N):
    l.append([])

for i in range(N):
    ligne = lineList[i]
    for j in range(N):
        l[j].append(ligne[j])

for i in range(X):
    l=Encodage(l)
affiche(l)