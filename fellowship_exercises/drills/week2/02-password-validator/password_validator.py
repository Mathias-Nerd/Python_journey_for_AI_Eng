def has_min_length(password):
    if len(password) < 8:
        return False
    return True


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special(password):
    return any(not(char.isupper() or char.islower() or char.isdigit() or char == " " ) for char in password)


def is_valid_password(password):
    return has_special(password) and has_min_length(password) and has_uppercase(password) and has_digit(password) and has_lowercase(password)


# print(is_valid_password("Mathias$$123"))

# bonus
def get_failed_requirements(password):
    # Write your code here
    pass