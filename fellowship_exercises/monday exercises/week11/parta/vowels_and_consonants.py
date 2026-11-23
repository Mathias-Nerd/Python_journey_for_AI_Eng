#Vowels and Consonants
#Write count_letters(text) that returns (vowels, consonants). Count only letters. Ignore spaces, digits and punctuation. Treat uppercase and lowercase the same.


def count_letters(text):
    vowels = ""
    consonants = ""
    for ch in text:
        if not (ch.lower() >= "a" and ch.lower() <= "z"):
            continue
        elif ch.lower() in "aeiou":
            vowels += ch
        else:
            consonants += ch
    
    
    return len(vowels), len(consonants)

print(count_letters("Hello, World 123"))
print(count_letters("AEIOU")            )
print(count_letters("rhythm"))
print(count_letters(""))

           
# count_letters("")                 