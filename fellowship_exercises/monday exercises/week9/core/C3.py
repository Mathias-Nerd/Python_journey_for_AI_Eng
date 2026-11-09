#The Recursive Toolkit
def digit_sum(n):
    if n < 10:
        return n

    return n % 10 + digit_sum(n //10)

def reverse_text(text):
    if len(text) <= 1:
        return text

    return  reverse_text(text[1:]) + text[0]


def count_char(text, ch):
    if len(text) <= 1:
        if text == ch:
            return 1

    add = 1 if text[0] == ch else 0
    return add + count_char(text[1:], ch)


def power(base, exp):
    if exp <= 1:
        return 0

    return base * power(base, exp -1)

    
# print(digit_sum(1234))
# print(reverse_text("abc"))
# print(count_char("banana", "a"))
print(pow(2, 10))