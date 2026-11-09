#3 by 3 sudoku


def sudoku_solver(board):

    # sol = []


    def find_empty_spaces(board):
        """
        Find all empty cells in a Sudoku board.

        Args:
            board: A 2D list representing the Sudoku board.
                Empty cells are represented by 0.

        Returns:
            A list of tuples containing (row, column) indices.
        """
        empty_spaces = []

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 0:
                    empty_spaces.append((row, column))

        return empty_spaces

    empty_spaces = find_empty_spaces(board)

    def solve(position):
        if len(empty_spaces) == 0:
            return "already solved"
        

        if position == len(empty_spaces):
            return board
        
        row, column = empty_spaces[position]

        
        for i in range(1,4):
            num = i

            def check_validity(board, row, column, num):
            # Check row
                if num in board[row]:
                    return False

                # Check column
                for i in range(len(board)):
                    if board[i][column] == num:
                        return False

                return True

        if check_validity(board, row, column, num):
            board[row][column] = num

            return solve(position + 1)

            board[row][column] = 0

    find_empty_spaces(0)
    return board


print(sudoku_solver([[0,1,0], [2,0,0], [0,0,3]]))


                