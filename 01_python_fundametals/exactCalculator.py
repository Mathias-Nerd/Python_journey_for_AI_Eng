"""

Implement exact_calculator(left, operator, right). Convert left and right to numbers. Support addition, subtraction, multiplication, division, remainder, and exponent. If either number cannot be converted, return Invalid number. If the operator is not supported, return Invalid operator. If division or remainder uses zero on the right side, return Cannot divide by zero. Round numeric results to 2 decimal places.
"""

def exact_calculator(left, operator, right):
    try:
        float(left)
        float(right)
    except:
        return "Invalid number"
    left = float(left)
    right = float(right)
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"
    if (operator == "/" or operator == "%") and right == 0:
        return "Cannot divide by zero"
    match operator:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            return round(left / right, 2)
        case "%":
            return round(left % right, 2)
        case "**":
            return left ** right
