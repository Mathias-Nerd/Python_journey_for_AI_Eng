"""
Write a recursive function in Python named count_char(s, char) that takes a string s and a single character char, and returns the total number of times char appears in s.
"""
# Author: Mathias Nerd


def count_char(s, char):
    if len(s) < 1:
        return 0
    if s[0] == char:
        return 1 + count_char(s[1:], char)
    else:
        return 0 + count_char(s[1:], char)


print(count_char("", "z"))
