"""
Implement reverse_string(value) without using slicing shorthand like [::-1]. Return a new string containing the input characters in reverse order.
"""

def reverse_string(value):
    reverse_string = ""
    for ch in value:
        reverse_string = ch + reverse_string
    return reverse_string


