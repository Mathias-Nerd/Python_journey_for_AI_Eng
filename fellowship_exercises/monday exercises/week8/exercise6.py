#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 6: Bubble sort (Best case and worst case)


number = [7,9,3,4,5]

def bubble_sort(num):
    swap = 0
    comparison = 0
    prev = num.copy()
    for i in range(len(num)):
        for j in range(0 , len(num) - i - 1):
            comparison += 1
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                swap += 1
        if num == prev:
            return f"{num}, with {comparison} comparisons and {swap} swap: "
        prev = num.copy()
        print(num)

    return f"{num}, with {comparison} comparisons and {swap} swap: "

print(bubble_sort(number))