#Mathias-Nerd
#09 - 11 - 2026
#Recursive Backtracking
#Subsets problem
#Generate all subsets of a given list

def subsets(num):
    res = []
    current = []
    def solve_subset(index):

        #Base case
        if index == len(num):
            res.append(current.copy())
            return

        #Case 1
        current.append(num[index])

        #Recurse (Explore)
        solve_subset(index + 1)

        #Undo
        current.pop()

        solve_subset(index + 1)


    solve_subset(0)
    return res



print(subsets([1,2,3]))