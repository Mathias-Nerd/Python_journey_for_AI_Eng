#Author: Mathias.Nerd
# Reverse with slicing + loop (two ways)
# Method A - Pythonic way:
# Use slicing you learned: s[::-1] to reverse. Save this to a variable reversed_slicing.

# def reverse_string(s):
#     rev = s[::-1]
#     return rev


# Method B:
def reverse_string(s):
    res = []
    for i in s:
        res.insert(0, i)
    ans = "".join(res)
    return ans
    





print(reverse_string("hello"))
print(reverse_string("Lagos"))
print(reverse_string("12345"))