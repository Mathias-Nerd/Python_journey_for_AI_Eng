#Mathias Nerd
#Question 1: Simple calculator
print("Welcome to a simple calculator program")
num1 = int(input("Enter a number: "))
operator = input("Enter an opertor: ")
num2 = int(input("Enter another number: "))

if operator == '+':
    print(f"Result: {num1+num2}")
elif operator == '-':
    print(f"Result: {num1-num2}")
elif operator == '*':
    print(f"Result: {num1*num2}")
elif operator == '/':
    if num2 == 0:
        print("Output: Cannot divide by zero")
    else:
        print(f"Result: {num1/num2}")
else:
    print("Invalid operator")


