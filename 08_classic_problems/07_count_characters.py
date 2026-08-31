#Author: Mathias.Nerd
#Count Character
def char_frequency(s):
    dic = {}
    norm_s = s.lower()
    for i in norm_s:
        if i == " ":
            continue
        else:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    return dic
print(char_frequency("hello"))
print(char_frequency("Lagos"))
print(char_frequency("aabbbc"))
print(char_frequency("a a a"))