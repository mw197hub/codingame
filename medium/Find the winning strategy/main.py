# https://www.codingame.com/ide/puzzle/find-the-winning-strategy

import sys,math,string


def calculateMex(Set): 
	Mex = 0; 
	while (Mex in Set): 
		Mex += 1
	return (Mex)

# A function to Compute Grundy Number of 'n' 
def calculateGrundy(n, Grundy): 
	Grundy[0] = 0
	Grundy[1] = 1
	Grundy[2] = 2
	Grundy[3] = 3

	if (Grundy[n] != -1): 
		return (Grundy[n])
	
	# A Hash Table 
	Set = set()
	for i in range(1, 4):
		Set.add(calculateGrundy(n - i, 
								Grundy))
	# Store the result 
	Grundy[n] = calculateMex(Set)
	return (Grundy[n])

# A function to declare the winner of the game 
def declareWinner(whoseTurn, piles, Grundy, n): 
	xorValue = Grundy[piles[0]]; 

	for i in range(1, n):
		xorValue = (xorValue ^ 
					Grundy[piles[i]]) 

	if (xorValue != 0): 	
		if (whoseTurn == 1): 
			return True
		else:
			return False
	else:
		if (whoseTurn == 1): 
			return True
		else:
			return False


def schrittVersuch(abstandList,col,gameList,schritt):
    piles=[];row=-1
    for j in range(len(abstandList)):
        abstand = abstandList[j]
        piles.append(abstand)
        if j == col:
            abstand = abstand - schritt
            row=gameList[col][0]+schritt
        
		
    return piles,row


##############################
#1
rows=2;columns=6
gameList=[[1, 5], [0, 5]]
gameList=[[1, 4], [1, 5]]
#gameList=[[1, 3], [2, 5]]
#2 
#rows=1;columns=30
#gameList=[[0, 29]]
#3
rows=5;columns=11
gameList=[[4, 6], [3, 7], [2, 8], [1, 9], [0, 10]]


###############################


while True:
    col=-1;row=-1;schritt=1;maxAbstand=-1
    abstandList = []
    for i in range(len(gameList)):
        columen = gameList[i]
        wert=columen[1] - columen[0] -1
        abstandList.append(wert)
        if wert > maxAbstand:
            col = i;maxAbstand=wert
	
    while True:
        piles,row = schrittVersuch(abstandList,col,gameList,schritt)

        n = len(piles) 
        maximum = max(piles)
        Grundy = [-1 for i in range(maximum + 1)]; 
        # Calculate Grundy Value of piles[i] and store it 
        for i in range(n):
            calculateGrundy(piles[i], Grundy); 

        if declareWinner(1, piles, Grundy, n):
            break
        schritt+=1


    print("{} {}".format(col,row))
    
    


#########
    break