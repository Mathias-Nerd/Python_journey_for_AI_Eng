#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 8:  Caesar Cipher
# Build a program that can encrypt and decrypt a message by shifting letters by a given number. For example, a shift of 1 makes 'a' become 'b', and 'z' becomes 'a'.  
print("Welcome to a Caeser Cipher program.")
word = input("Enter word: ").strip()
try:
    shift = int(input("Enter number of shift: ").strip())
except:
    print("Wrong shift input.")
mode = input("Enter mode ('encrypt' or 'decrypt'): ").strip().lower()
result = ""

if mode in ["encrypt", "decrypt"]:
    shift_progression = shift if mode == "encrypt" else -shift
    
    # print(f"Shift progression : {shift_progression}")
    for ch in word:
        if ch.isalpha():
            if ch.isupper():
                start = ord('A')
            else:
                start = ord('a')
            ch_position = (ord(ch) - start)
            new_position = (ch_position + shift_progression) % 26
            result += chr(start + new_position)
        else:
            result += ch
        # print(f"result {result}")
    print(f"The {mode}ed word is: {result}")
else:
    print("Wrong mode input.")