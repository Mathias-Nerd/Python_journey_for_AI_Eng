#Roman to integer
#


#This code checks numerical order but didn't validate Roman numeral rules.
def roman_to_integer(numeral):
    rom = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    sum = 0
    i = 0
    while i < len(numeral):
        if i + 1 < len(numeral) and rom[numeral[i]] < rom[numeral[i+1]]:
            sum -= rom[numeral[i]]
        else:
            sum += rom[numeral[i]]
        i += 1

    return sum
print(roman_to_integer("III"))