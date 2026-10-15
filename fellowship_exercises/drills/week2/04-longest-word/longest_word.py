def longest_word(sentence):
    sentence = sentence.strip()
    if sentence == "":
        return sentence
    list_of_words = sentence.split()
    cleaned_list = []
    for word in list_of_words:
        word = word.strip(" .,_-?!")
        cleaned_word = ""
        for index, ch in enumerate(word):
            if ch.isalnum() or (index != 0):
                cleaned_word += ch
        cleaned_list.append(cleaned_word)
    word_length = {}
    highest = 0
    for word in cleaned_list:
        length = len(word)
        if length > highest:
            highest = length
        word_length[word] = length
    for key, value in word_length.items():
        if value == highest:
            return key




print(longest_word("the quick brown fox"))
        


# bonus
def longest_words(sentence):
    sentence = sentence.strip()
    if sentence == "":
        return []
    list_of_words = sentence.split()
    cleaned_list = []
    for word in list_of_words:
        word = word.strip(" .,_-?!")
        cleaned_word = ""
        for index, ch in enumerate(word):
            if ch.isalnum() or (index != 0):
                cleaned_word += ch
        cleaned_list.append(cleaned_word)
    word_length = {}
    highest = 0
    
    for word in cleaned_list:
        length = len(word)
        if length > highest:
            highest = length
        word_length[word] = length
    result = []
    for key, value in word_length.items():
        if value == highest:
            result.append(key)
    return result
