#Given a paragraph of text, count how many times each word appears and store it in a dictionary. Then find and print the single most frequent word


def count_words(words: list[str]) -> dict[str, int]:
    res = {}
    word_list = words.lower().strip().split()
    for word in word_list:
        temp = word.strip(".,!")
        if temp in res:
            res[temp] += 1
        else:
            res[temp] = 1

    return res


def most_frequent(freq: dict[str, int]) -> str:
    highest_value = 0
    highest_key = ""
    for key, value in freq.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
    return f"Most frequent word: {highest_key} ({highest_value})"


word = "Python is fun, and Python is powerful!"
freq_table = count_words(word)
print(most_frequent(freq_table))