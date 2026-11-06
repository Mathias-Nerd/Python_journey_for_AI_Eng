#Mathias Nerd
#Practicing Recursion
#EXercise 1 :  Subsets problem

"""
Subset generation
Level: Easy

Difficulty: 3/10

Your task:
- Generate all subsets of [1, 2, 3].
- Use include/exclude choices.
- Store all solutions.
- Return the list of subsets.
What you're practising: Recursion, choices, base cases, saving copies, and undoing decisions.
"""

def find_subsets(nums):
    result = []
    current = []

    #Recursive backtrackig function
    def subset(index):

        #Base case
        if index == len(nums):
            # print(f"Current: {current}")
            temp = current.copy()
            result.append(temp)
            # print(f"result: {result}")
            return

        #Recursive case

        #Choice 1

        current.append(nums[index])

        #Explore
        subset(index + 1)

        #Choice 2
        current.pop()

        #Explore
        subset(index + 1)
        

    subset(0)


    return result

print(find_subsets([1, 2, 3]))