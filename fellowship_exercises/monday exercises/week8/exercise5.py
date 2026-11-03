#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 5: Tower of hanoi


def hanoi(n, source, target, helper):
    if n == 1:
        return [(source, target)]
    return hanoi(n-1, source, helper, target) + [(source, target)] + hanoi(n-1, helper, target, source)

print(hanoi(3,"A", "C", "B" ))

for i in range(1, 11):
    print(len(hanoi(i, "A", "C", "B")))