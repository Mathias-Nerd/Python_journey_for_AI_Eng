#Pascal triangle
def pascal_triangle(n):
    if n == 0:
        return []
    res = []
    prev = 0
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
for item in result:
    temp = ""
    for i in range(0, len(item)):
        temp += str(item[i])
        if not (i == len(item) - 1):
            temp += " "
    print(f"{temp:^9}")
    