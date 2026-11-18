#Mathias-Nerd
#Week 10
#Word break

def word_break(s, word_dict):
    if s == "":
        return True

    temp = ""

    for i in range(len(s)):
        temp += s[i]
        if temp in word_dict:
            return word_break(s[i+1:], word_dict)


    return False


print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))