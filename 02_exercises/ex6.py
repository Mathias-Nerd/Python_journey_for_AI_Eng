""""
The Task
Write a factory function create_pipeline(operation_type) that returns a stateful inner function that processes numbers.
Requirements
The outer function initialises a call counter variable set to 0.
The inner function accepts *args (a variable number of numerical arguments).
Use the nonlocal keyword inside the inner function so the counter increases by 1 on every run.
Before returning the calculated output, print a status message:
"Execution #[count]: Processed [N] items." (where N is len(args)).
Use Python's match/case statement on operation_type to handle processing:
"double": returns a list with every number multiplied by 2.
"square": returns a list with every number squared.
"summarise": returns the sum() of all numbers.
_ (wildcard/default case): prints "Invalid operation" and returns None.
"""
def create_pipeline(operation_type):
    counter = 0
    def stateful_function(*args):
        nonlocal counter
        counter += 1
        print(f"Execution {counter}: Processed {len(args)} items")
        

    return stateful_function()