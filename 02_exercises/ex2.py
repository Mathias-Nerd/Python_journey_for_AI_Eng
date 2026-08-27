#Take a string representing an account number or ID. Obscure all but the last 4 characters with asterisks (*). If the string is shorter than 4 characters, return "Invalid Input".
def obscure(id):
    if len(id) < 4:
        return id
    else:
        lent = len(id)-4
        return f"{'*'*lent}{id[-4:]}"
print(obscure("Math"))
