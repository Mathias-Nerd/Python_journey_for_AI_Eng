#Run Length

def rle_encoding(text):
    result = ""
    prev = ""
    # count = 0
    if len(text) == 0:
        return text
    i = 0
    while i < len(user_input):
        if i == 0:
            result += user_input[i]
            prev = user_input[i]
            count = 1
        else:
            if user_input[i] == prev:
                count += 1
            else:
                result += str(count)
                result += user_input[i]
                count = 1
                prev = user_input[i]
        i += 1
    result += str(count)
    print(result)


def rle_decode(text):
    i = 0
    res = ""
    num = ""
    while i < len(text):
        if text[i].isalpha():
            if len(num) != 0:
                current = "".join([letter] * int(num))
                res += current
                num = ""
                letter = text[i] 
            else:
                letter = text[i]
        elif text[i].isdigit():
            num += text[i]
        i += 1
        # if i % 2 != 0:
        # i += 1
    res += "".join([letter] * int(num))
    return res
            


user_input = "aab"
rle_encoding(user_input)

print(rle_decode("a4b3c2"))