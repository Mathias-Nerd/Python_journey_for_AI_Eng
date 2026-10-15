#Mathias_Nerd
#Fellowship week4 exercise1: Palindrome

def is_letter(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')
    

def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        while left < right and not is_letter(word[left]):
            left += 1
        while left < right and not is_letter(word[right]):
            right -= 1
        if word[left].lower() != word[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
    
    
print("Welcome to palindrome checker.")
word = input("Enter sentence: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not palindrome")
    