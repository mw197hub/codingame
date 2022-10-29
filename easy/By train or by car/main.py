import sys,math

def getZeit(t):
    m = "0"+str(int(t % 60))
    zeit = str(int(t/60))+":"+m[-2:]
    return zeit

def speed(km,kmh):
    erg = (km*60/kmh)
    m = int(erg)
    s = (erg - m) * 0.6
    return erg

fList=['Paris Orleans 133', 'Orleans Tours 218']
fList=['Orleans Blois 63', 'Cholet Clisson 35.9 ', 'Tours Saumur 78', 'Clisson Nantes 33.7', 'Blois Tours 65', 'Angers Cholet 65', 'Saumur Angers 66']

zielList=['Pithiviers', 'Cholet']
fList=['Poitiers Angouleme 138', 'Pithiviers Orleans 57', 'Orleans Blois 63', 'Blois Tours 65', 'Bordeaux Périgueux 137', 'Tours Saumur 78', 'Saumur Angers 66', 'Angers Cholet 65']

zielList=['Angouleme', 'Royan']
fList=['Angouleme Jarnac 33.2', 'Jarnac Cognac 11', 'Cognac Saintes 28.1', 'Saintes Saujon 27.7', 'Saujon Royan 13.3']



newList=[];start=zielList[0];ziel=zielList[1]
while True:
    for f in fList:
        place = f.split(" ")
        if start == place[0]:
            newList.append(f)
            start= place[1]
            break
    tList = newList[-1].split(" ")
    if zielList[1] == tList[1]:
        break
print(newList,file=sys.stderr)

train=65.0 - 8.0
car=0.0

for f in newList:
    place = f.split(" ")
    if float(place[2]) > 6:
        train += speed(6,50)
        train += speed(float(place[2])-6,284)
    else:
        train += speed(float(place[2]),50)
    train += 8
    if float(place[2]) > 14:
        car += speed(14,50)
        car += speed(float(place[2])-14,105)
    else:
        car += speed(float(place[2]),50)

print(train,file=sys.stderr)
print(car,file=sys.stderr)

if train < car:
    print("TRAIN "+getZeit(train))
else:
    print("CAR " + getZeit(car))