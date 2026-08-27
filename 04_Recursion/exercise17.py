def square(lst):
    # answer = [x*x for x in lst]
    answer = map(lambda x: x**2, lst)
    return list(answer)


print(square([1, 2, 3, 4, 5, 6, 7]))


#sequence
#conditional (if, goto, case)
#iteration (for loop, while loop)
#function