#Mathias-Nerd
#Felloshio exercise 
#Week3: Question 2 (Palindrome using 2 pointers)
print("Welcome to a palindrome checker.")

word = input("Enter a sentence: ").lower()
is_palindrome = True


left = 0
right = len(word) - 1

while left < right:
    while left < right and not word[left].isalnum():
        left += 1
        
    while left < right and not word[right].isalnum():
        right -= 1
    
    
    if word[left] != word[right]:
        is_palindrome = False
        break
        
    left += 1
    right -= 1
    
print("Palindrome" if is_palindrome else "Not a palindrome")
    
        



