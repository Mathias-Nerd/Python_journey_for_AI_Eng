#Mathias Nerd
#Palindrome Checker Program
print("Welcome to a palindrome checker problem.")

#Taking input word
word = input("Enter a word: ")
rev_word = ""   #An empty string to store reversed word

#The loop that does the reverse
for ch in word:
    rev_word = ch + rev_word

print(f"{word} is a palindrome" if word == rev_word else f"{word} is not a palindrome")
