""""
Author : Mathias Nerd
Write a function analyse_user_tags(user1_raw, user2_raw) that cleans messy tag entries from two different users, removes duplicate tags, and identifies shared and unique interests between them.
"""

# This function cleans the data and converts it to a set


def clean(data):
    splitted_value = data.split(",")
    stripped_list = list(map(lambda x: x.strip(), splitted_value))
    lowercase_list = list(map(lambda m: m.lower(), stripped_list))
    return set(lowercase_list)


def analyse_user_tags(user1_raw, user2_raw):
    set1 = clean(user1_raw)
    set2 = clean(user2_raw)

    common_items = set1 & set2
    all_unique_items = set1 | set2
    user1_unique_items = set1 - set2
    user2_unique_items = set2 - set1

    return {"user1_unique_count": len(user1_unique_items), "user2_unique_count": len(
        user2_unique_items), "shared_interests": common_items, "all_interests": all_unique_items}


user1 = "  python , CODING, Data , python,  AI "
user2 = "coding ,  Web , AI ,  JavaScript , AI "

result = analyse_user_tags(user1, user2)
print(result)
