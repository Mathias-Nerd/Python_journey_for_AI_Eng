#Mathias-Nerd
#10 - 11 - 2026
#Backtracking
#Subsets problem: Generate all subsets of a given list

def subset(num):
    """This function returns a list of all subsets of a given list"""

    res = [] #This variable contains all subsets
    temp = [] #This variable holds the current subset at a particular time

    def solve(index):
        """The recursive backtracking function that computes the subset"""

        #BASE CASE
        if index == len(num):
            res.append(temp.copy())
            return

        #CHOICE 1
        temp.append(num[index])

        #EXPLORE
        solve(index+1)

        #BACKTRACK(undo)
        temp.pop()

        #CHOICE 2
        solve(index+1)


    solve(0)
    return res


print(subset([1, 2, 3]))