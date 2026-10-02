#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 5: word frequency
#Given a paragraph of text, count how many times each word appears and store it in a dictionary. Then, find and print the single most frequent word. 

print("Welcome to a word frequency program.")
sentence = input("Enter a sentence: ").lower()
cleaned_sentence = ""
word_freq = {}
for ch in sentence:
    if ch.isalpha() or ch == " ":
        cleaned_sentence += ch
word_list = cleaned_sentence.split()
for word in word_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
highest = 0
for word, freq in word_freq.items():
    if freq > highest:
        highest = freq
        most_freq = word
print(f"The single Word with the highest frequency is {wor} ")