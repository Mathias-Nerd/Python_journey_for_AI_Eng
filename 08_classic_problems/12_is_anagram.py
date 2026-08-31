#Author: Mathias.Nerd

# Write a function is_anagram(s, t) that takes two strings s and t and returns True if t is an anagram of s, and False otherwise.
# An Anagram is a word formed by rearranging the letters of a different word.
# Case-insensitive, ignore spaces.
# Examples:
# is_anagram("listen", "silent") -> True
# is_anagram("race", "care") -> True
# is_anagram("hello", "world") -> False
# is_anagram("Astronomer", "Moon starer") -> True
def is_anagram(s, t):
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()
    s_dic = {}
    t_dic = {}
    for ch in s:
        if ch in s_dic:
            s_dic[ch] += 1
        else:
            s_dic[ch] = 1
    for ch in t:
            if ch in t_dic:
                t_dic[ch] += 1
            else:
                t_dic[ch] = 1
    return s_dic == t_dic

print(is_anagram("listen", "silent"))
print(is_anagram("race", "care"))
print(is_anagram("hello", "world"))
print(is_anagram("Astronomer", "Moon starer"))