#Mathias-Nerd
#09 - 11 - 20226
#Recursive Backtracking
#N queens 
"""
Write a function n_queens(n) that solves the 4×4 N-Queens problem and returns all possible solutions.

Requirements
1. Create a 4×4 board.
2. Place exactly one queen in each row.
3. No two queens should share a column or diagonal.
4. Use backtracking to explore possible positions.
5. Store every valid solution.
6. Return all solutions.
Constraints
- Use 0 for empty cells and 5 for queens.
- Do not use external libraries.
- Save independent copies of the board.
- Your solution should work for different values of n, not just 4.
"""


def check_validity(board, row, column):
    
    # Check the column above
    for i in range(row):
        if board[i][column] == 5:
            return False

    # Check the upper-left diagonal
    for i, j in zip(
        range(row - 1, -1, -1),
        range(column - 1, -1, -1)
    ):
        if board[i][j] == 5:
            return False

    # Check the upper-right diagonal
    for i, j in zip(
        range(row - 1, -1, -1),
        range(column + 1, len(board))
    ):
        if board[i][j] == 5:
            return False

    return True

def n_queens(n):
    #Creating board

    row = [0] * n
    board = []
    for i in range(n):
        board.append(row)

    def check 

    def solve_n_queens(row):
        for column in range(n):
            







    return board

print(n_queens(4))