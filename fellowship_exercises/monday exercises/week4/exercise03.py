#Question3: Word frequency
"""
Given a paragraph of text, count how many times each word appears and store it in a dictionary. Then find and print the single most frequent word.
Examples
Input: "Python is fun, and Python is powerful!"
Output: Most frequent word: python (2)
Constraints
Treat uppercase and lowercase as the same.
Strip basic punctuation (commas, periods) manually — no re, no string.punctuation.
Create two pure functions: count_words(words: list[str]) -> dict[str, int] and most_frequent(freq: dict[str, int]) -> str.
count_words builds a fresh dict and mutates nothing from outside.
most_frequent returns the most frequent word; a for loop is allowed.
No max() on the dictionary. No sorting. No collections.Counter.
Do not import libraries.
"""

def count_words(words):
    words = words.lower()
    dict = {}
    cleaned_sentence = ""
    for ch in words:
        if ch.isalpha() or ch == " ":
            cleaned_sentence += ch
    cleaned_sentence = cleaned_sentence.split()
    for word in cleaned_sentence:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


def most_frequent(freq):
    highest = 0
    highest_word = ""
    for word, index in freq.items():
        if index > highest:
            highest = index
            highest_word = word
    return highest_word

sentence = input("Enter a word: ")
sentence_freq = count_words(sentence)
# print(sentence_freq)
print(f"Most frequent word is: {most_frequent(sentence_freq)}")
