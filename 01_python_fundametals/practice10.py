#Valid Palindrome
#Author: Mathias Nerd 
#Date: 20 Aug 2026
#Write a function that accepts a string s and returns True if it is a palindrome, or False otherwise.
#Do not use built-in string reversal methods (e.g., s[::-1] or reversed()). 
# Implement your own character inspection logic (e.g., using a two-pointer approach).$1 \le \text{length}(s) \le 2 \times 10^5$
# The solution should run in $O(n)$ time complexity using $O(1)$ extra memory space.

def valid_palindrome(s):
    s = s.lower().replace(" ", "").replace(".", "").replace(",", "")
    #Base case
    if len(s) == 0 or len(s) == 1:
            return True
    #Recursive case
    if not(s[0] == s[-1]):
        return False
    else:
        return valid_palindrome(s[1:-1])

print(valid_palindrome("ma"))