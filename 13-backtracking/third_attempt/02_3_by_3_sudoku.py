#Mathias-Nerd
#10-11-2026
#Backtracking
#3 X 3 Sudoku solver

"""
Given a 3 × 3 Sudoku board, complete the empty cells so that:
1. Every row contains the numbers 1, 2 and 3 exactly once.
2. Every column contains the numbers 1, 2 and 3 exactly once.
3. Every cell must contain a valid number.
4. Existing numbers (clues) must not be changed.
"""


def sudoku_3X3_solver(board):


    def get_empty_spaces(board):
        empty = []
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == 0:
                    position = (row, column)
                    empty.append(position)
        return empty

        

    def is_placeable(board, row, column, num):

        #Row check
        if num in board[row]:
            return False

        #Column check
        for row in board:
            if num == row[column]:
                return False

        return True


    def solve(index):

        #BASE CASE
        if index == len(empty):
            return board
        
        row, column = empty[index]
        res = None
        #CHOOSE
        for num in range(1, len(board) + 1):
            if is_placeable(board, row, column, num):
                board[row][column] = num

                #RECURSE
                res = solve(index+1)

                if res is not None:
                    return res
                
                #BACKTRACK
                board[row][column] = 0


        return res

    empty = get_empty_spaces(board)
    outcome = solve(0)
    return board if outcome is  not None else "The board has no solution"
    # return empty


print(sudoku_3X3_solver([[1,2,0], [0,3,0], [0, 1, 2]]))