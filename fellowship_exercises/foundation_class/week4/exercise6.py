#Caesar Cipher
#Encrypt or decrypt a message by shifting letters. Shift of 1: 'a' → 'b', 'z' → 'a'.


def make_shift(shift_number):

    def shifted_char(ch):
        start = ord('a') if ch.islower() else ord('A')
        current_position = ord(ch) - start
        new_position = (current_position + shift_number) % 26
        new_character = chr(start + new_position)
        return new_character

    return shifted_char




def shift(word, shift_number, mode):
    shift_number = shift_number if mode == "encrypt" else -shift_number
    shift = make_shift(shift_number)
    new_word = "".join(list(map(shift, word)))
    return new_word


print("Welcome to Caesar Cipher.")
word = input("Enter word: ")
shift_number = int(input("Enter shift number: "))
choice = input("Type the action you want to perform (encrypt or decrypt)").lower()

print(shift(word, shift_number, choice))