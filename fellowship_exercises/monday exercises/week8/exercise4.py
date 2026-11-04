#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 4: Integer to Roman

def integer_to_roman(number):
    rom = [
        [1000 , "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"] 
    ]
    res = ""
    i = 0
    while i < len(rom):
        divisor, string = rom[i]
        if number // divisor:
            count = number // divisor
            res = res + (string * count )
            number = number % divisor
        i += 1

    return res


print(integer_to_roman(3999))