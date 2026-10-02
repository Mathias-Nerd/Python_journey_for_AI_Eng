"""
Age Calculator - Expanded Challenge (Levels 1-4)

Asks for a birthdate (YYYY-MM-DD) and shows:
  - exact age in years, months and days
  - total days, hours and minutes alive
  - days until next birthday
  - zodiac sign
  - day of the week you were born
"""

import calendar
from datetime import date, datetime, time


# ---------------------------------------------------------------------------
# Level 3: input + validation
# ---------------------------------------------------------------------------
def get_birthdate():
    """Keep asking until the user enters a real, non-future date."""
    while True:
        text = input("Enter your birthdate (YYYY-MM-DD): ").strip()

        try:
            # strptime raises ValueError for bad formats AND impossible
            # dates like 2023-02-29 or 2023-13-05
            birth = datetime.strptime(text, "%Y-%m-%d").date()
        except ValueError:
            print("  That's not a valid date. Use YYYY-MM-DD, e.g. 1995-08-15.\n")
            continue

        if birth > date.today():
            print("  That date is in the future. Please try again.\n")
            continue

        return birth


# ---------------------------------------------------------------------------
# Level 2 + 3: exact years / months / days
# ---------------------------------------------------------------------------
def calculate_age(birth, today):
    """Return (years, months, days) between birth and today."""
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    # Not enough days? Borrow the length of the previous month.
    # calendar.monthrange knows about leap years, so February is handled.
    if days < 0:
        months -= 1
        if today.month == 1:
            prev_year, prev_month = today.year - 1, 12
        else:
            prev_year, prev_month = today.year, today.month - 1
        days += calendar.monthrange(prev_year, prev_month)[1]

    # Not enough months? Borrow a year.
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


# ---------------------------------------------------------------------------
# Level 4 helpers
# ---------------------------------------------------------------------------
def days_until_next_birthday(birth, today):
    """Days from today until the next birthday (0 if it's today)."""

    def birthday_in(year):
        try:
            return date(year, birth.month, birth.day)
        except ValueError:
            # Born on Feb 29 and `year` isn't a leap year -> use Mar 1
            return date(year, 3, 1)

    next_bday = birthday_in(today.year)
    if next_bday < today:
        next_bday = birthday_in(today.year + 1)
    return (next_bday - today).days


def zodiac_sign(birth):
    """Return the Western zodiac sign for a birth month and day."""
    # (last month, last day, sign) - each sign runs until this date
    signs = [
        (1, 19, "Capricorn"),
        (2, 18, "Aquarius"),
        (3, 20, "Pisces"),
        (4, 19, "Aries"),
        (5, 20, "Taurus"),
        (6, 20, "Gemini"),
        (7, 22, "Cancer"),
        (8, 22, "Leo"),
        (9, 22, "Virgo"),
        (10, 22, "Libra"),
        (11, 21, "Scorpio"),
        (12, 21, "Sagittarius"),
    ]
    for last_month, last_day, sign in signs:
        if (birth.month, birth.day) <= (last_month, last_day):
            return sign
    return "Capricorn"  # Dec 22 - Dec 31


def plural(number, word):
    """1 -> '1 year', 2 -> '2 years'"""
    return f"{number} {word}" if number == 1 else f"{number} {word}s"


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------
def main():
    birth = get_birthdate()
    now = datetime.now()
    today = now.date()

    years, months, days = calculate_age(birth, today)
    print(
        f"\nYou are exactly {plural(years, 'year')}, "
        f"{plural(months, 'month')}, and {plural(days, 'day')} old."
    )

    # Total time alive
    total_days = (today - birth).days
    seconds_alive = (now - datetime.combine(birth, time.min)).total_seconds()
    total_hours = int(seconds_alive // 3600)
    total_minutes = int(seconds_alive // 60)
    print(f"That's {total_days:,} days, {total_hours:,} hours, "
          f"or {total_minutes:,} minutes alive.")

    # Next birthday
    left = days_until_next_birthday(birth, today)
    if left == 0:
        print("Happy birthday! Today is your birthday!")
    else:
        print(f"Your next birthday is in {plural(left, 'day')}.")

    # Zodiac + weekday
    print(f"Your zodiac sign is {zodiac_sign(birth)}.")
    print(f"You were born on a {birth.strftime('%A')}.")


if __name__ == "__main__":
    main()


get_birthdate()