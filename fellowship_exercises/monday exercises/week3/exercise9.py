#Mathias-Nerd
#Felloshio exercise 
#Week3: Question 9: Reverse a given integer. For example, 12345 becomes 54321.

print("Welcome to a number reverser program.")
num = int(input("Enter number: "))
sign = -1 if num < 0 else 1
num = abs(num)
rev_num = 0
while num > 0:
    last_digit = num % 10
    rev_num = rev_num * 10 + last_digit
    num = num // 10
    
rev_num *= sign
print(f"Reversed num = {rev_num}")