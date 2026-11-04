#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 7: Pascal Triangle

def pascal_triangle(n):
    if n == 0:
        return []
    
    res = []
    prev = []

    for i in range(1, n+1):
        sub = []

        for j in range(0,i):
            if j == 0 or j == i-1:
                sub.append(1)
            else:
                sub.append(prev[j] + prev[j-1])

        prev = sub
        res.append(sub)

    return  res


n = 5
result = pascal_triangle(n)

# Calculate the width needed for the widest row
width = len(" ".join(map(str, result[-1])))

for item in result:
    temp = " ".join(map(str, item))
    print(temp.center(width))
    