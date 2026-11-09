#Mathias-Nerd
#09 - 11 - 2026
#Recursive Backtracking
#3 by 3 sudoku


"""
find_empty_spaces(board) — already covered.
check_validity(board, row, column, num) — already covered.
solve_sudoku(board) — combine everything using backtracking.
Handle an already-solved board.
Handle a board with no possible solution.
"""

def sudoku(board):

    def get_empty_spaces(board):
        empty = []
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 0:
                    empty.append((row, column))
        return empty

    def is_valid(board, row, column, num):
        #row check
        if num in board[row]:
            return False

        #Column check
        for item in board:
            if item[column] == num:
                return False

        #Box check
        # starting_row = (row//3) * 3
        # starting_column = (column//3) * 3

        # for i in range(starting_row, starting_row + 3):
        #     for j in range(starting_column, starting_column + 3):
        #         if board[i][j] == num:
        #             return False

        return True

    
    empty_spaces = get_empty_spaces(board)

    def solve_sudoku(index):
        #Base case
        if index == len(empty_spaces):
            return board
        
        row, column = empty_spaces[index]


        for num in range(1,4):
            if is_valid(board, row, column, num):
                board[row][column] = num
                result = solve_sudoku(index + 1)

                if result is not None:
                    return result

                board[row][column] = 0
        return None
                




    
    result = solve_sudoku(0)

    return "No solution" if result is None else result

print(sudoku([[1,0,0], [0,2,0], [0,0,3]]))