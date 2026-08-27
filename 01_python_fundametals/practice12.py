#Valid parenthesis
# #Author: Mathias Nerd 
#Date: 20 Aug 2026
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
def valid_parenthesis(s):
    opening_par = ["(", "{", "["]
    closing_par = [")", "}", "]"]
    stack = []
    dic = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    for char in s:
        if char in opening_par:
            stack.append(char)
        elif char in closing_par:
            if len(stack) == 0 or dic[char] != stack[-1]:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(valid_parenthesis("([)]"))