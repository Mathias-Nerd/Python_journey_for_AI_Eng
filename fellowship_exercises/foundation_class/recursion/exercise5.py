#Given a string, write a recursive function that returns the string in reverse order.

def reverse_string(text):
    if text == "":
        return text
    return reverse_string(text[1:]) + text[0]

print(reverse_string("hello"))