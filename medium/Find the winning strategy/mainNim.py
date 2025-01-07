''' Game Description- 
"A game is played between two players and there are N piles 
of stones such that each pile has certain number of stones. 
On his/her turn, a player selects a pile and can take any 
non-zero number of stones upto 3 (i.e- 1,2,3) 
The player who cannot move is considered to lose the game 
(i.e., one who take the last stone is the winner). 
Can you find which player wins the game if both players play 
optimally (they don't make any mistake)? " 

A Dynamic Programming approach to calculate Grundy Number 
and Mex and find the Winner using Sprague - Grundy Theorem.

	piles[] -> Array having the initial count of stones/coins 
			in each piles before the game has started. 
n	 -> Number of piles 

Grundy[] -> Array having the Grundy Number corresponding to 
			the initial position of each piles in the game 

The piles[] and Grundy[] are having 0-based indexing'''

PLAYER1 = 1
PLAYER2 = 2

# A Function to calculate Mex of all
# the values in that set 
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
	
		if (whoseTurn == PLAYER1): 
			print("Player 1 will win\n"); 
		else:
			print("Player 2 will win\n"); 
	else:
	
		if (whoseTurn == PLAYER1): 
			print("Player 2 will win\n"); 
		else:
			print("Player 1 will win\n"); 
	
# Driver code
if __name__=="__main__":
	
	# Test Case 1 
	piles = [ 2,3] 
	n = len(piles) 

	# Find the maximum element 
	maximum = max(piles)

	# An array to cache the sub-problems so that 
	# re-computation of same sub-problems is avoided 
	Grundy = [-1 for i in range(maximum + 1)]; 

	# Calculate Grundy Value of piles[i] and store it 
	for i in range(n):
		calculateGrundy(piles[i], Grundy); 

	declareWinner(PLAYER1, piles, Grundy, n); 

	''' Test Case 2 
	int piles[] = {3, 8, 2}; 
	int n = sizeof(piles)/sizeof(piles[0]); 


	int maximum = *max_element (piles, piles + n); 

	// An array to cache the sub-problems so that 
	// re-computation of same sub-problems is avoided 
	int Grundy [maximum + 1]; 
	memset(Grundy, -1, sizeof (Grundy)); 

	// Calculate Grundy Value of piles[i] and store it 
	for (int i=0; i<=n-1; i++) 
		calculateGrundy(piles[i], Grundy); 

	declareWinner(PLAYER2, piles, Grundy, n); '''

# This code is contributed by rutvik_56
