"""
Drill 06: Recursive Palindrome Check
Module: 01-recursion
"""


def is_palindrome(text: str, left: int = 0, right: int | None = None) -> bool:
    """
    Recursively determines if a string is a palindrome using two pointers.

    Args:
        text (str): String to check.
        left (int): Left index pointer.
        right (int | None): Right index pointer.

    Returns:
        bool: True if text is a palindrome, False otherwise.

    Raises:
        TypeError: If text is not a string.
    """
    # TODO: Implement validation, base cases, and two-pointer recursive convergence
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if right == None:
        right = len(text) - 1
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    else:
        return is_palindrome(text, left + 1, right - 1)


print(is_palindrome("a"))
