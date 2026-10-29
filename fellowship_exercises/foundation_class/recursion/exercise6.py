#Write a recursive function that determines whether a given string is a palindrome.
def is_palindrome(text):
    if len(text) == 1 or len(text) == 0:
        return True
    if text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])


word = input("Enter text: ")
print(f"{word} is a palindrome." if is_palindrome(word.lower()) else f"{word} is not a palindrome.")
