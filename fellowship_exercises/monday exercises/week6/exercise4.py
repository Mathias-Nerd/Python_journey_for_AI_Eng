#Mathias-Nerd
#Monday exercise: week 6
#Question 4: balanced brackets

# user_input = input("Enter input: ")
user_input = "(a + b) * [c - d]"

def valid_brackets(user_input):
    brackets = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    check_stack = []
    
    for ch in user_input:
        if ch in brackets.values(): #opening brackets
            check_stack.append(ch)
        elif ch in brackets.keys(): #closing brackets
            if len(check_stack) != 0  and check_stack[-1] == brackets[ch]:
                check_stack.pop()
            else:
                check_stack.append(ch)

    if len(check_stack)== 0: 
        return "Balanced"
    else:
        return "Not balanced"
    # return check_stack


print(valid_brackets(user_input))