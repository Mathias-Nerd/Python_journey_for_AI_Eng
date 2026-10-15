#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 7: Anagram Finder 
# Check if two words are anagrams of each other (meaning they contain the exact same characters in the exact same frequencies, just in a different order). 

print("Welcome to an anagram finder program.")
word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()
word1_dict = {}
word2_dict = {}

for ch in word1:
    if ch in word1_dict:
        word1_dict[ch] +=1
    else:
        word1_dict[ch] = 1

for ch in word2:
    if ch in word2_dict:
        word2_dict[ch] +=1
    else:
        word2_dict[ch] = 1

print("Anagram." if word1_dict == word2_dict else "Not an anagram.")