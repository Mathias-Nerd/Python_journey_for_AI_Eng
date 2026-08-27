"""
Implement first_and_last(value). Return a dictionary with two keys: "first" and "last". "first" should contain the first character of the string. "last" should contain the last character of the string. If the string is empty, return {"first": "", "last": ""}.
"""

def first_and_last(value):
    result_dict = {
        "last" : "",
        "first" : ""
    }
    if len(value) == 0:
        return result_dict
    result_dict["last"] = value[-1]
    result_dict["first"] = value[0]
    return result_dict

