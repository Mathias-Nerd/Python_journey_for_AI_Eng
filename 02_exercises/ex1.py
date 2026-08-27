#Write a function that takes a string and a target character, counts how many times the character appears (case-insensitive), and determines if that count is even or odd.
def case_insensitive(word, ch):
    count = 0
    for i in word:
        if i == ch:
            count += 1
        if count % 2 == 0:
            result = "Even"
        else:
            result = "Odd"
    return f"The word {word} contains {result} occurence of {ch}"

print(case_insensitive("Massachussetts", "s"))
