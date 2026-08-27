#Filtering Even Numbers
numbers = [12, 5, 8, 19, 21, 4, 10]
res = filter(lambda x : x % 2 == 0 ,numbers)
print(list(res))
