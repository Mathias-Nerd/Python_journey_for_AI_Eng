#Compose and Pipe
#Write two higher-order functions: compose(f, g) → returns a function computing f(g(x)); pipe(*funcs) → returns a function applying functions left-to-right: pipe(f, g, h)(x) == h(g(f(x))). Then build a small text pipeline: strip whitespace → lowercase → remove vowels → reverse.


def compose(f, g): 

    def compute(x):
        return f(g(x))

    return compute


def pipe(*funcs):

    def compute(x):
        for func in funcs:
            x = func(x)
        return x
    return compute

def strip(word):
    return word.strip()

def lower(word):
    return word.lower()

def remove_vowels(word):
    res = ""
    for ch in word:
        if ch.lower() not in "aeiou":
            res += ch
    return res

def reverse(word):
    res = ""
    for ch in word:
        res = ch + res
    return res


add_one = lambda x: x + 1
double = lambda x: x * 2

pipeline = pipe(strip, lower, remove_vowels, reverse)
print(pipeline(" Hello World "))