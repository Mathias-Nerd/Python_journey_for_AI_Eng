#Filter and captalise
names = ["alice", "bob", "charlie", "david", "ed"]
#filter
filtered_names =list( filter(lambda x: len(x) >= 4, names ))
upper_names = list(map(lambda m: m.upper() ,filtered_names))
print(upper_names)
