#Mathias-Nerd
#10-11-2026
#Backtracking
#3 X 3 Sudoku solver b

"""
Given a 3 × 3 Sudoku board, write a function that returns every possible valid solution without changing the original clues.
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

    sol = []

    def solve(index):

        #BASE CASE
        if index == len(empty):
            temp = []
            for row in board:
                temp.append(row.copy())
            sol.append(temp)
            return 
        
        row, column = empty[index]
        res = None
        #CHOOSE
        for num in range(1, len(board) + 1):
            if is_placeable(board, row, column, num):
                board[row][column] = num

                #RECURSE
                res = solve(index+1)

                # if res is not None:
                #     return res
                
                #BACKTRACK
                board[row][column] = 0


        return res

    empty = get_empty_spaces(board)
    outcome = solve(0)
    return sol 
    # return empty



result = sudoku_3X3_solver([[0,0,3], [0,0,3], [0, 0, 0]])
if result == []:
    print("There is no valid solution")
else:
    for solution in result:
        for row in solution:
            print(row)
        print()
        

