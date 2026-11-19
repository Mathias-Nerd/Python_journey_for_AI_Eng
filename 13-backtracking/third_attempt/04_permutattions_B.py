#Mathias-Nerd
#11 - 11 - 2026
#Recursive Backtracking
#Permutations: Generat all permutations of number
# A CONVENTIONAL BACKTRACKING APPROACH (Choose → Explore → Undo)


def permutation(nums):
    res = []
    current = []

    def solve():
        if len(current) == len(nums):
            res.append(current[:])
            return

        for num in nums:

            if num in current:
                continue

            #CHOICE
            current.append(num)

            #RECURSE
            solve()

            current.pop()

    solve()

    return res

print(permutation([1, 2, 3]))


