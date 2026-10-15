def first_non_repeating(s, case_sensitive=True):
    ch_count = {}
    for ch in s:
        if ch not in ch_count:
            ch_count[ch] = 1
        else:
            ch_count[ch] += 1
    # print(ch_count)
    
    if 1 in ch_count.values():
        for key, value in ch_count.items():
            if value == 1:
                return key
    else:
        return None

print(first_non_repeating(""))