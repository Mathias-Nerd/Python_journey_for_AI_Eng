#Two sum
def two_sum(nums, target):
    checked_numbers = {}
    res = []
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        diff = target - numbers[i]
        if diff in checked_numbers:
            res.append(checked_numbers[diff])
            res.append(i)
            # print(f"[{checked_numbers[diff]}, {i}]")
            return res
        else:
            checked_numbers[numbers[i]] = i

print("Welcome to two sum program.")
numbers = input("Enter a list of numbers separated by space: ").split()
target = int(input("Enter target: "))

print(two_sum(numbers, target))