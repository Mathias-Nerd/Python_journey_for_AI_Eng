#Mathias-Nerd
#Week 10: Question 4
#Josephus Survivor: Circular Elimination

def josephus(n, k):

    if n == 0:
        return 1

    return (josephus(n-1, k) + k )% n

   

    
print(josephus(7, 3))