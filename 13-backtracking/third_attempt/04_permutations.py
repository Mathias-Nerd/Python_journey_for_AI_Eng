#Mathias-Nerd
#11 - 11 - 2026
#Recursive Backtracking
#Permutations: Generat all permutations of number

# A RECURSIVE DECOMPOSITION APPROACH (Remove → Solve → Reconstruct → Restore)

def permutations(nums):
    res = []
    #BASE CASE
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):

        n = nums.pop(0)

        sub_perms = permutations(nums)

        for items in sub_perms:
            items.append(n)

        res.extend(sub_perms)
        nums.append(n)

    return res

print(permutations([1, 2, 3]))



            
