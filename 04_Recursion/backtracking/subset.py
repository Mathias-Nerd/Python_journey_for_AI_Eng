def subset(num, index = 0, res = [], temp = []):

    #Base case
    if index == len(num):
        res.append(temp.copy())
        return res

    #Recursive case

    #Choice 1
    temp.append(num[index])

    #Recurse
    res = subset(num, index + 1, res, temp)

    #Choice 2
    temp.pop()

    #Recurse
    res = subset(num, index + 1, res, temp)

    return res


print(subset([1,2]))
