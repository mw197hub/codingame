
#class Solution:
#    def nimGame(self, piles: List[int]) -> bool:
#        xor_sum = 0
#        for pile in piles:
#            xor_sum ^= pile
#        return xor_sum != 0

from typing import List
from functools import lru_cache

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        # Apply memoization to avoid recomputation of the same game states
        @lru_cache(maxsize=None)
        def can_win(st):
            # Convert tuple to list to modify the piles
            piles_list = list(st)
            # Iterate over each pile
            for i, pile in enumerate(piles_list):
                # Try removing 1 to pile stones from the current pile
                for stones_removed in range(1, pile + 1):
                    # Remove the stones for the current move
                    piles_list[i] -= stones_removed
                    # Check if opponent would lose from this state
                    if not can_win(tuple(piles_list)):
                        return True  # If opponent loses, current player wins
                    # Undo the move
                    piles_list[i] += stones_removed
            # If no winning move, return False
            return False

        # Start the game with the initial piles configuration
        return can_win(tuple(piles))

# Example usage:
sol = Solution()
result = sol.nimGame([1,3,5,7,9,5,4,12])  # Pass the initial piles as a list
print(result)  # Outputs True or False depending on whether you can win the Nim game