"""
The Goal: Write a recursive function print_countdown(n) that prints numbers from n down to 1, followed by "Blastoff!".
"""
# Author: Mathias Nerd


def print_countdown(n):
    if n <= 0:
        print("Blastoff!")
        return 
    print(n)
    return print_countdown(n-1)


print_countdown(3)


"""
def print_countdown(2):
    if n <= 0:
        print("Blastoff!")
        return 
    print(n)
    return print_countdown(n-1)

    print2




    def print_countdown(1):
    if n <= 0:
        print("Blastoff!")
        return 
    print(n)
    return print_countdown(n-1)

    prints 1

     def print_countdown(0):
        if n <= 0:
            print("Blastoff!")
            return 
        print(n)
        return print_countdown(n-1)

"""