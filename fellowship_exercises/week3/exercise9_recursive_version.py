#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 9: Reverse a given integer. For example, 12345 becomes 54321. (Recursive version)



def rev_num(num, result = 0):
    if num == 0:
        return result
    last_digit = num % 10
    result = result * 10 + last_digit
    return rev_num(num // 10, result)


print("Welcome to a number reverser program.")
num = int(input("Enter number: "))
sign = -1 if num < 0 else 1
num = abs(num)
ans = rev_num(num) * sign
print(ans)