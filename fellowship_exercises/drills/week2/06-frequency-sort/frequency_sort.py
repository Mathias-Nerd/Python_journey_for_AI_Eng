def frequency_sort(items):
    sorted_list = sorted(items)
    freq_dict = {}
    for item in sorted_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    sorted_dict = sorted(freq_dict.items(), key = lambda x: x[1], reverse=True )
    result = []
    for num, freq in sorted_dict:
        for i in range(freq):
            result.append(num)
    return result



# print(frequency_sort([1, 2, 2, 1, 3]))