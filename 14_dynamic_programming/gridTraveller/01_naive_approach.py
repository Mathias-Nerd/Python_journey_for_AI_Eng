#Mathias-Nerd
#20-11-2026
#Dynamic Programming: Grid Traveller
#Naive recursive approach

"""Python Exercise: Grid Traveller (Memoization)
Task: Implement a memoized function called grid_traveller(rows, columns) that returns the number of possible ways to travel from the top-left corner to the bottom-right corner of a grid.

You can only move:
- RIGHT (one column forward).
- DOWN (one row forward)."""


def gridTraveller(row, column):

    #Base case

    if row == 1 and column == 1: return 1
    if row == 0 or column == 0: return 0

    return gridTraveller(row-1, column) + gridTraveller(row, column -1)


print(gridTraveller(2,3))