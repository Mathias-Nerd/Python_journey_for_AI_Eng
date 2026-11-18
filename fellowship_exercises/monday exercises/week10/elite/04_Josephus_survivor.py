#Mathias-Nerd
#Week 10: Question 4
#Josephus Survivor: Circular Elimination

def josephus(n, k):

    if n == 0:
        return 1

    next_safe_position = josephus(n-1, k) #getting the next safe position

    move_forward = next_safe_position + k 
    wrap = move_forward % n

    return wrap

print(josephus(5, 2))