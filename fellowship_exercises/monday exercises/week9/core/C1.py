#Week 9 Core 1 
def is_balanced(text):
    stack = []
    dic = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    opening_par = set(dic.values())
    closing_par = set(dic.keys())
        

    for char in text:
        if char in opening_par:
            stack.append(char)
        elif char in closing_par:
            if len(stack) == 0 or dic[char] != stack[-1]:
                return False
            else:
                stack.pop()

    return len(stack) == 0

print(is_balanced("(a + b) * [c - d]") )
print(is_balanced("{[()]}")   )
print(is_balanced("([)]")   )
print(is_balanced("((")  )
print(is_balanced("}{") )
print(is_balanced("") )