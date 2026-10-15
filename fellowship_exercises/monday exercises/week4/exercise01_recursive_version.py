#Mathias-Nerd
#Question1 : Palindrome


def is_palindrome(text):
    if len(text) <= 1:
        return True
    if not is_letter(text[0]):
        return is_palindrome(text[1:])
    if not is_letter(text[len(text)-1]):
        return is_palindrome(text[:len(text)-1])
    
    if text[0] != text[len(text)-1]:
        return False
    return is_palindrome(text[1:-1])    



def is_letter(ch):
    if ch.isalpha():
        return True
    return False

word = input("Enter a sentence: ").lower()
print(is_palindrome(word))