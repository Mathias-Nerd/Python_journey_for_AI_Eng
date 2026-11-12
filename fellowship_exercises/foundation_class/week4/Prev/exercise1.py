#11-11-2026
#For foundations class
#Palindrome with 2 pointer logic


def is_letter(ch):
    if ch.isalpha():
        return True
    return False

# def is_palindrome(word):
#     left = 0
#     right = len(word) - 1

#     while left < right:
#         while (not is_letter(word[left])) and left  < right:
#             left += 1 

#         while (not is_letter(word[right])) and right > left:
#             right -= 1

#         if word[left].lower() != word[right].lower():
#             return False
        
#         left += 1
#         right -= 1

#     return True




def is_palindrome(word, left = 0, right = None):
    if right == None:
        right = len(word) - 1

    if left >= right:
        return True

    if (not is_letter(word[left])) and left  < right:
        return is_palindrome(word, left + 1, right)

    if (not is_letter(word[right])) and left < right:
        return is_palindrome(word, left, right - 1)

    if word[left].lower() == word[right].lower():
        return is_palindrome(word, left + 1, right - 1)
    

    return False



res = is_palindrome("Was it a car or a cat I saw?")
print("Palindrome" if res else "Not a palindrome")
