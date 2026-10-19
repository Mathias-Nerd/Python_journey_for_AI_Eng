#Mathias-Nerd
#Monday exercise: week 6
#Question 8: Run-Length Encoding
#Given a string, compress it using run-length encoding: replace consecutive repeated characters with the character followed by the count.
def run_length_encoding(text):
    result = ""
    prev = ""
    # count = 0
    for i in range(len(user_input)):
        if i == 0:
            result += user_input[i]
            prev = user_input[i]
            count = 1
        else:
            if user_input[i] == prev:
                count += 1
            else:
                result += str(count)
                result += user_input[i]
                count = 1
                prev = user_input[i]
    result += str(count)
    print(result)


user_input = "aaabbbcccaaa"
run_length_encoding(user_input)
