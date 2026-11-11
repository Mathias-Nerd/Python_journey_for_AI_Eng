"""
Drill 03: Announce Execution Order
Module: 04-decorators-and-closures
"""


def announce(log_list: list[str]) -> callable:
    """
    Decorator logging DECORATION, BEFORE, and AFTER milestones.
    """
    # TODO: Implement parametric decorator appending to log_list at correct lifecycle phases


    def decorator(func):
        nonlocal log_list
        log_list.append("DECORATION")

        def wrapper(*args, **kwargs):
            log_list.append("BEFORE")
            res = func(*args, **kwargs)
            log_list.append("AFTER")
            return res

        return wrapper

    return decorator
    


events = []


@announce(events)
def add(a,b):
    global events
    events.append("RUNNING...")
    return a + b

res = add(2,3)
print(f"Res = {res}")

print(f"Events: {events}")