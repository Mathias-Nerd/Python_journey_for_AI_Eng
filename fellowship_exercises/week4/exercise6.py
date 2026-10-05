#Caesar Cipher

#make_multiplier = lambda n: lambda x: x * n

"""
def outer():
    def inner():
        print("Hello")

    return inner

func = outer()
func()
"""

def make_shifter(shift):
    if mode in ["encrypt", "decrypt"]:
        shift_progression = shift if mode == "encrypt" else -shift
    def per_character(ch):
        if ch.isalpha():
            if ch.isupper():
                start = ord('A')
            else:
                start = ord('a')
            ch_position = (ord(ch) - start)
            new_position = (ch_position + shift_progression) % 26
            shifted_char = chr(start + new_position)
        else:
            shifted_char += ch
        return  shifted_char
    return per_character





word = input("Enter word: ").strip()
try:
    shift = int(input("Enter number of shift: ").strip())
except:
    print("Wrong shift input.")
mode = input("Enter mode ('encrypt' or 'decrypt'): ").strip().lower()

calc_shift = make_shifter(shift)
x = list(map(calc_shift, word))
res = "".join(x)
print(res)