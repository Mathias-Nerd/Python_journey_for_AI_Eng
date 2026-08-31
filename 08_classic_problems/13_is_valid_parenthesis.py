#Author: Mathias.Nerd
# Write a function is_valid_parentheses(s) that takes a string containing only ()[]{} and returns True if the string is valid.
# A string is valid if brackets are closed in correct order.
"""
is_valid_parentheses Algorithm - Steps
You need a stack (list where you only append and pop) to track open brackets.

1. Create dict for mapping close -> open:
    pairs = { ')': '(', ']': '[', '}': '{' }
2. Create empty stack: stack = []
3. Loop each char ch in s:
4. If ch is an opening bracket ( [ { :
    push it: stack.append(ch)
5. If ch is a closing bracket ) ] } :
    Check if stack is empty? If empty, no opener to match -> return False
    Pop top: top = stack.pop()
    Check if top != pairs[ch] (does top match this closer?)
    If not match -> return False
6. After loop, check stack: if stack is empty, all opened were closed -> True, else False
"""
def is_valid_parentheses(s):
    pairs = { ')': '(', ']': '[', '}': '{' }
    stack = []
    for ch in s:
        if ch in ["(", "[", "{"]:
            stack.append(ch)
        if ch in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            if stack[-1] != pairs[ch]:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(is_valid_parentheses("()"))
print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))
print(is_valid_parentheses("([)]"))
print(is_valid_parentheses("{[]}"))

