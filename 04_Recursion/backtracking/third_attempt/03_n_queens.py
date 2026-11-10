##Mathias-Nerd
#10 - 11 - 2026
#Backtracking
#N Queens Problem: Given a number n, place n queens on an n×n chessboard so that no two attack each other (same row, column, or diagonal). Return all valid arrangements, where each solution shows the column position of the queen in each row.

def n_queens(n):
    """This function returns all possible ways of arranging n queens on n X n chess board"""


    res = []   
    queen_val = 5
    #Create chess board
    board = []
    for i in range(n):
        temp = [0] * n
        board.append(temp)


    #Checking if it is safe to place the queen
    def is_valid_placement(board, row, col, queen_val):
        n = len(board)

        # 1. Row Check: Does 5 exist in this row?
        if queen_val in board[row]:
            return False

        # 2. Column Check: Does 5 exist in this column?
        for r in range(n):
            if board[r][col] == queen_val:
                return False

        # 3. Diagonal Checks: Do any 5s exist along the two diagonals?
        for r in range(n):
            for c in range(n):
                if board[r][c] == queen_val:
                # Check main and anti-diagonals relative to (row, col)
                    if abs(r - row) == abs(c - col):
                        return False

        return True
    


    def solve(row):
        #BASE CASE
        if row == len(board):
            temp = []
            for row in board:
                temp.append(row.copy())
            res.append(temp)
            return

        for column in range(n):
            #CHOICE
            if is_valid_placement(board, row, column, queen_val):
                board[row][column] = queen_val

                #RECURSE
                solve(row + 1)

                #BACKTRACK
                board[row][column] = 0

        

                

        

        













    solve(0)
    return res if res is not None else "No result"

n = 5
solution = n_queens(n)
#printing result
for result in solution:
    for row in result:
        print(row)
    print()
