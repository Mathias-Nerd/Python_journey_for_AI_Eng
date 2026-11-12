#Write a program that determines whether a full sentence reads the same forwards and backwards, ignoring mixed casing, spaces, and punctuation

def is_letter(ch: str) -> bool:
    if ch.isalpha():
        return True

    return False

def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:

        #Manually skipping spaces and punctuation from left
        if not is_letter(text[left]):
            left += 1
            continue

        #Manually skipping spaces and punctuation from right
        if not is_letter(text[right]):
            right -= 1
            continue

        #performing comparison
        if text[left].lower() != text[right].lower():
            return False

        #Moving pointers
        left += 1
        right -= 1


    return True


res = is_palindrome("Was it a car or a cat I saw?")
print("Palindrome" if res else "Not a palindrome")