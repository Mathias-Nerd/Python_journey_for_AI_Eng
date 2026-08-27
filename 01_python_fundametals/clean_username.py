"""
Implement clean_username(value). The function should remove leading and trailing spaces, convert the text to lowercase, and replace every space with an underscore. Return the cleaned username.
"""

def clean_username(value):
    remove_spaces = value.strip()
    lower_value = remove_spaces.lower()
    replace_value = lower_value.replace(" ", "_")
    return replace_value
