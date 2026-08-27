# Author: Mathias Nerd
"""
Write a recursive function in Python named is_palindrome(s) that takes a string s and returns True if s is a palindrome (reads the same forwards and backwards) and False otherwise.
"""
"""
#Basic version
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
"""

#Added a layer of stripping and converting to lower
def is_palindrome(s):
    s = s.strip().lower()
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print(is_palindrome("RACAR"))
