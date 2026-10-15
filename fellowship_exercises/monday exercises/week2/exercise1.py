#Fellowship exercise
#Week 2
#Simple calculator

print("WElcome to a simple calculator program.")
num1 = (input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = (input("Enter second number: "))
try:
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"{num1} / {num2} = {round(num1 / num2)}")
    elif operator == '*':
        print(f"{num1} X {num2} = {num1 * num2}")
    else:
        print("Invalid operator")
except:
    print("Something broke your code, probably you entered somthing that is not a number")