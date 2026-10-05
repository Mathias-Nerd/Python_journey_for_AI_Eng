#Number 10
#Build a program that analyzes a list of financial transactions. Your program should calculate total income, total expenses, balance, largest expense, number of expenses, and overall financial status.

transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "Salary", "amount": 500000, "type": "income"},
    {"name": "Internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "Food", "amount": 45000, "type": "expense"}
]

def calculate_total(lst):
    total = 0
    for i in lst:
        total += i
    return total

def get_income(transactions):
    def is_income(item):
        if item["type"] == "income":
            return True
        else:
            return False
    return list(filter(is_income, transactions))

income_list = get_income(transactions)

#Calculate total income
income_amounts = list(map(lambda x: x["amount"], income_list ))
# print(income_amounts)
total_income = calculate_total(income_amounts)
print(f"Total income: {total_income}")



def get_expenses(transactions):
    def is_expense(item):
        if item["type"] == "expense":
            return True
        else:
            return False
    return list(filter(is_expense, transactions))
expense_list = get_expenses(transactions)
expense_amounts = list(map(lambda x: x["amount"], expense_list ))
number_of_expenses = len(expense_amounts)

total_expenses = calculate_total(expense_amounts)
print(f"Total expenses: {total_expenses}")

    

print(f"Number of expenses: {number_of_expenses}")

# def find_largest():
#     pass

# def get_balance():
#     balance = total_income - total_expenses
#     return balance
# balance = (get_balance)

# print(f"Balance: {balance}")

# def get_status():
#     if balance > 0:
#         return "Positive balance"
#     else:
#         return "Negative balance"

# print(get_status())