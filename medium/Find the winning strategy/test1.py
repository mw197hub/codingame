import sys,math

def sprague_grundy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n - 1) % 2

def possible_moves(n):
    moves = []
    if n > 1:
        moves.append(n - 1)
    if n % 2 == 1:
        moves.append(n - 2)
    return moves

def analyze_game(positions):
    game_values = []
    for position in positions:
        value = 0
        for i in range(1, position + 1):
            value ^= sprague_grundy(i)
        game_values.append(value)
    return game_values

# Beispiel:
positions = [3, 4]
game_values = analyze_game(positions)
print(game_values)