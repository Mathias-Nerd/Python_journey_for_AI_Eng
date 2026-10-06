#Mathias-Nerd
#Fellowship exercise week 4
#Question 10: Build a program that analyzes a list of financial transactions. Your program should calculate total income, total expenses, balance, largest expense, number of expenses, and overall financial status.


"""
Do not use external libraries.
Do not modify the original transactions list.
Break the solution into small, focused functions.
Your analysis functions should return values rather than print them.
Keep printing/output outside the analysis functions.
Create: get_income, get_expenses, calculate_total, find_largest, get_balance, and get_status.
get_income returns only income transactions.
get_expenses returns only expense transactions.
Use filter at least once.
Use map at least once to extract amounts.
calculate_total must calculate the total manually; do not use sum().
find_largest must find the largest expense manually; do not use max() or sorted().
The original list must remain unchanged.
Handle no transactions, no expenses, and a balance of exactly 0.
"""

transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "Salary", "amount": 500000, "type": "income"},
    {"name": "Internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "Food", "amount": 45000, "type": "expense"}
]

def get_income(transactions):
    income_list = filter(lambda x: True if x["type"] == "income" else False, transactions)
    return list(income_list)


def get_expenses(transactions):
    expense_list = filter(lambda x: True if x["type"] == "expense" else False, transactions)
    return list(expense_list)




def calculate_total(trans_list):
    sum = 0
    amount = list(map(lambda x: x["amount"], trans_list))
    for item in amount:
        sum += item
    return sum

def find_largest(transactions):
    largest = 0
    largest_trans = ""
    for item in transactions:
        if item["amount"] > largest:
            largest_trans = item["name"]
            largest = item["amount"]
    return f"{largest_trans} ({largest})"





def get_balance(income, expense):
    return income - expense

def get_status(balance):
    return "Positive balance" if balance > 0 else "Negative balance"


income_list = get_income(transactions)
expenses_list = get_expenses(transactions)
total_income = calculate_total(income_list)
total_expenses = calculate_total(expenses_list)
balance = get_balance(total_income, total_expenses)
largest_expense = find_largest(expenses_list)
status = get_status(balance)

print(f"Total income: {total_income}")
print(f"Total expenses:{total_expenses}")
print(f"Balance: {balance}")
print(f"Largest expense: {largest_expense}")
print(f"Number of expenses: {len(expenses_list)}")
print(f"Status: {status}")