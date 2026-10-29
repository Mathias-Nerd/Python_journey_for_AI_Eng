"""
Drill 03: Recursive String Reversal
Module: 01-recursion
"""


def reverse_string(text: str) -> str:
    """
    Recursively reverses a string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    # TODO: Implement validation, base cases, and head/tail recursive step
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if text == "":
        return text
    return reverse_string(text[1:]) + text[0]

# print(reverse_string("hello"))
