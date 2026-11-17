#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 9: Subsets and permutations (Backtracking)

def subsets(items):

    res = []
    current = []
    def solve(index):
        #BASE CASE
        if index == len(items):
            res.append(current.copy())
            return

        #INCLUDE
        current.append(items[index])
        solve(index + 1)
        
        #BACKTRACK
        current.pop()
        solve(index + 1)

    solve(0)
    return res


def permutations(items):

    res = []
    current = []

    def solve(index):
        if index == len(items):
            res.append(current.copy())
            return

        for item in items:
            if item not in current:
                current.append(item)
                solve(index + 1)

                current.pop()
        




    solve(0)
    return res

print(subsets([1,2,3]))
print(permutations([1,2,3]))