"""
Implement str_len(value) without using len(). Count the characters manually and return the number of characters in the string.
"""
def str_len(value):
    count = 0
    for ch in value:
        count += 1
    return count

