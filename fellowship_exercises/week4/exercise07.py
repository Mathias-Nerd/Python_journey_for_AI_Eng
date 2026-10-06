#Mathias-Nerd
#Number 7
#Compose and pipe
#Write two higher-order functions: 
# compose(f, g) → returns a function computing f(g(x)); 
# pipe(*funcs) → returns a function applying functions left-to-right: pipe(f, g, h)(x) == h(g(f(x))). 
# Then build a small text pipeline: strip whitespace → lowercase → remove vowels → reverse.

"""
Examples
add_one = lambda x: x + 1
double  = lambda x: x * 2
compose(add_one, double)(5)   # 11
pipe(add_one, double)(5)      # 12

pipeline = pipe(strip, lower, remove_vowels, reverse)
pipeline("  Hello World  ")
"""

def compose(f, g):
    def composed(x):
        return f(g(x))

    
    return composed


def pipe(*funcs):
    def piped(x):
        for func in funcs:
            x = func(x)
        return x


    return piped


def strip(x):
    return x.strip()


def lower(x):
    return x.lower()


def remove_vowels(x):
    vowels = "AEIOUaeiou"
    res = ""
    for ch in x:
        if ch not in vowels:
            res += ch
    return res


def reverse(x):
    res = ""
    for ch in x:
        res = ch + res
    return res






add_one = lambda x: x + 1
double = lambda x: x * 2


print(compose(add_one, double)(5))
print(pipe(add_one, double)(5))

pipeline = pipe(strip, lower, remove_vowels, reverse)
print(pipeline("   Hello world     "))