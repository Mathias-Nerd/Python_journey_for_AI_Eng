"""
Implement manual_palindrome(text). Ignore spaces and letter case. Return true if the cleaned text reads the same forward and backward, otherwise return false. Do not use slicing shorthand or reversed. Students may need to research manual string reversal.
"""


def manual_palindrome(text):
    text = text.replace(" ", "")
    text = text.lower()
    text_reverse = ""
    for ch in text:
        text_reverse = ch + text_reverse
    if text == text_reverse:
        return True
    else:
        return False


