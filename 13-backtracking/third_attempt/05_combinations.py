#Mathias-Nerd
#11 - 11 - 2026
#Recursive Backtracking
#Combinations: Given a list of distinct numbers, return all possible combinations of size k

def combinations(nums, k):
    res = []
    current = []

    def solve(start):

        #BASE CASE
        if len(current) == k:
            res.append(current[:])
            return

        for i in range(start, len(nums)):
            #CHOICE
            current.append(nums[i])

            #RECURSE
            solve(i + 1)

            #BACKTRACK
            current.pop()


    solve(0)

    return res

print(combinations([1,2,3,4], 3))