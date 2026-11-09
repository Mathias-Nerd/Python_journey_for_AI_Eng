#Mathias Nerd
#Practicing Recursion
#EXercise 2: N queens

"""
2. N-Queens (4 × 4)
Intermediate

Difficulty: 6/10

Your task:
- Place 4 queens on a 4 × 4 board.
- No two queens should attack each other.
- Find and return all valid solutions.
What you're practising: Constraint checking, 2D state management, recursive exploration, and backtracking.
"""



def n_queens(n):

    #Create board
    board = []
    for i in range(n):
        temp = [0] * n
        board.append(temp)

    

    #Check validity
    


    sol = []
    
    def solve(row):
        #BASE CASE
        if row == n:
            sol.append([row.copy() for row in board])
            return
            

        #RECURSIVE CASE
        for column in range(n):

            #Check for validity
            def check_validity(board, row, column):
                # Check the column
                for i in range(row):
                    if board[i][column] == 5:
                        return False
        
                # Check upper-left diagonal
                for i, j in zip(range(row - 1, -1, -1),range(column - 1, -1, -1)):
                    if board[i][j] == 5:
                        return False
        
                # Check upper-right diagonal
                for i, j in zip(range(row - 1, -1, -1),
                                range(column + 1, len(board))):
                    if board[i][j] == 5:
                        return False

            
                return True
            #End of validity check function
            
            if check_validity(board, row, column):
                result = board[row][column] = 5


                #recurse
                result = solve(row + 1)

                # if result is not None:
                #     return result
            
                #Backtrack
                board[row][column] = 0



            


    solve(0)
    return sol
# print(n_queens(4))
result = n_queens(4)
for v_result in result:
    for row in v_result:
        print(row)
    print()


