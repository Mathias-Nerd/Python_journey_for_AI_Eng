"""
Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator". If the operator is "/" or "%" and b is 0, return "Cannot divide by zero". Round division results to 2 decimal places.
"""
def safe_calculator(a, operator, b):
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"
    else:
        if (operator == "/" or operator == "%") and b == 0:
            return "Cannot divide by zero"
        match operator:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return round(a / b, 2)
            case "%":
                return round(a % b, 2)
            case "**":
                return a ** b
