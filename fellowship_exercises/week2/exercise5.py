#Fellowship exercise
#Week 2
#Word frequency

input_word = input("Enter a sentence: ").lower()

#The list containing each word
new_word_list = input_word.split(" ")
answer_dict = {}
for word in new_word_list:
    if word in answer_dict:
        answer_dict[word] += 1
    else:
        answer_dict[word] = 1
for key, value in answer_dict.items():
    print(f"{key} : {value}") 

