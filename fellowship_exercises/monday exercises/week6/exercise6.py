#Mathias-Nerd
#Monday exercise: week 6
#Question 6: Write a program that determines whether a given year is a leap year. A year is a leap year if it is divisible by 4, and it is not divisible by 100 unless it is also divisible by 400.
def leap_year():
    while True:
        year = input("Enter year: ").strip()
        try:
            year = int(year)
        except ValueError:
            print("Enter a valid year.")
            continue
        break
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
                print(f"{year} is a leap year")
            # else:
            #     print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

leap_year()