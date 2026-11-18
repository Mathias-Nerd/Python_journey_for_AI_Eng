#Mathias-Nerd
#Week 10: Question 3
#Recursive expression evaluator

# def evaluate(expr, index = 0):


#     if index == len(expr) - 1:
#         return int(expr[index]) 

#     if index == len(expr):
#         return 0


#     if expr[index].isdigit():
#         index += 1

#     # if expr[index] == "*":
#     #     prod = int(expr[index-1]) * int(expr[index + 1])

#     #     # return prod + evaluate(expr, index + 2)

#     if expr[index] == "+":
#         return int(expr[index-1]) + evaluate(expr, index + 1)
#     else:
#         return int(expr[index-1]) - evaluate(expr, index +1)        

# print(evaluate("8-2-2"))