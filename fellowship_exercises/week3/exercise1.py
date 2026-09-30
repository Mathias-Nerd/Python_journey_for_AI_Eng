#Mathias-Nerd
#Week 3 Fellowship exercise
#Question 3: continuous calculator
#Build a continuous calculator that maintains a running total. The user inputs an operator and a number repeatedly (e.g., + 5, then * 2). 


#Initial values
result  = 0
history = []


#The loop that makes the program going
while True:
    user_input = input("Enter operation (+ 5, * 2, undo, quit): ").strip()

    #Quitting the program
    if user_input.lower() == "quit":
        break

    if user_input.lower() == "undo":
        if history:
            result = history.pop()
            print(result)
        else:
            print("There is nothing to undo.")
        continue

    user_entry = user_input.split()
    if len(user_entry) != 2:
        print("Wrong input. Enter operator operand (e.g + 5, * 2, undo, quit): ")
        continue

    operator, operand = user_entry

    #Checking for valid operator
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator")
        break

    #To catch when somethig that is not a number is entered
    try:
        operand = float(operand)
    except:
        print("Invalid number.")
        continue

    if operator == "/" and operand == 0:
        print("Cannot divide by zero.")
        continue

    history.append(result)

    match operator:
        case "+":
            result += operand
        case "-":
            result -= operand
        case "*":
            result *= operand
        case "/":
            result /= operand

    print(result)