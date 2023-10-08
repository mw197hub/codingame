def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Überprüfen, ob die Zahl 'num' in der Zeile, Spalte oder im 3x3-Unterquadrat bereits vorhanden ist.
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Wenn die Zelle leer ist, versuche, eine Zahl einzusetzen.
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Rekursiver Aufruf für die nächste Zelle.
                            return True
                        board[row][col] = 0  # Zurücksetzen, wenn keine Lösung gefunden wird.
                return False  # Keine gültige Lösung für diese Zelle gefunden.
    return True  # Das Sudoku wurde erfolgreich gelöst.

# Beispiel-Sudoku-Rätsel
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sboard = [['8', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '3', '6', '0', '0', '0', '0', '0'], ['0', '7', '0', '0', '9', '0', '2', '0', '0'], ['0', '5', '0', '0', '0', '7', '0', '0', '0'], ['0', '0', '0', '0', '4', '5', '7', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '3', '0'], ['0', '0', '1', '0', '0', '0', '0', '6', '8'], ['0', '0', '8', '5', '0', '0', '0', '1', '0'], ['0', '9', '0', '0', '0', '0', '4', '0', '0']]
for x in range(9):
    for y in range(9):
        sudoku_board[x][y] = int(sboard[x][y])


if solve_sudoku(sudoku_board):
    print("Sudoku gelöst:")
    print_board(sudoku_board)
else:
    print("Keine Lösung gefunden.")
