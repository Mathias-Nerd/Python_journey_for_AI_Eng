#01 Knapsack (without DP)
#The Naive Approach
"""
Test	Weights	        Values	      Capacity	  Expected answer
1	    [1, 3, 4, 5]	[1, 4, 5, 7]	  7	        9
2	    [2, 3, 4]	    [3, 4, 5]	      5	        7
3	    [4, 5, 6]	    [10, 12, 15]	  3	        0
4	    [1, 2, 3]	    [10, 15, 40]	  3	        40
5	    [2, 2, 3, 4]	[3, 4, 5, 6]	  6	        10
"""

def knapsack(weights, values, capacity, index=0):
    #Base case
    if index == len(weights):
        return 0

    #exclude
    exclude = knapsack(weights, values, capacity, index + 1)


    #include
    include = 0
    if  weights[index] <= capacity:
        include = values[index] + knapsack(weights, values, capacity - weights[index], index + 1 )



    return max(include, exclude)
weight, values, capacity = [1, 3, 4, 5]	,[1, 4, 5, 7]	,  7	  
print(knapsack(weight, values, capacity))