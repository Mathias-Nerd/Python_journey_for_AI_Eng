#Mathias-Nerd
#Week 4: Question 4
#Determine whether a string contains balanced parentheses. Every opening parenthesis '(' must have a matching closing parenthesis ')' in the correct order.
# You only need to handle round parentheses; ignore other character types.
user_input = input("Enter an expression: ").strip()

counter = 0
for ch in user_input:
    if counter < 0:
        break
    if ch in ["(", ")"]:
        if ch == "(":
            counter += 1
        else:
            counter -= 1
print("Balanced" if counter == 0 else "Not balanced")
