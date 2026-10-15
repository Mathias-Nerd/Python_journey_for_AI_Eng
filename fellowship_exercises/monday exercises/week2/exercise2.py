#Fellowship exercise
#Week 2
#Palindrome

word = input("Enter any word: ").lower()
rev_word = ""
for ch in word:
    rev_word = ch + rev_word
print("Palindrome" if word == rev_word else "Not a palindrome")