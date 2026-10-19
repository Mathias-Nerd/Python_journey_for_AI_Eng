#Mathias-Nerd
#Monday exercise: week 6
#Question 5: To-Do List Mini Project — Extended
def todo_list():
    todo = []
    possible_options = ["add" , "remove" , "done" , "quit" , "view" ]
    print("Menu: add | view | remove | done | quit\n")
    while True:
        user_input = input("> ").strip().split()
        choice, *items = user_input
        choice = choice.lower()
        items = " ".join(items)
        if len(user_input) == 0:
            continue
        if len(user_input) == 1 and choice in possible_options[3:]:
            menu = user_input[0].lower()
            if menu == "view":
                if len(todo) == 0:
                    print("No item in the todo list.\n")
                else:
                    for i in range(len(todo)):
                        print(f"{i+1}. {todo[i][1]} {todo[i][0]}")
                    print()
            elif menu == "quit":
                print("Goodbye!")
                break
        elif len(user_input) > 1:
            if user_input[0].lower() in possible_options[:3]:
                menu = user_input[0].lower() 
                if menu == "add":
                    sentence = items.capitalize()
                    if len(sentence) != 0:
                        item = []
                        item.append(sentence)
                        item.append("[ ]")
                        todo.append(item)
                        print("Task added\n")
                elif menu == "done":
                    if  len(user_input[1:]) == 1:

                        try:
                            number = int(user_input[1])
                        except:
                            print("Wrong value entered, enter a whole number.\n")
                            continue
                        if number <= len(todo):
                            todo[number-1][1] = "[x]"
                            print(f"Task {number} marked as done.\n")
                        else:
                            print(f"You have only {len(todo)} items in your todo.\n")
                    else:
                        print("Wrong item number entered\n")
                        continue
                elif menu == "remove":
                    if  len(user_input[1:]) == 1:
                        try:
                            number = int(user_input[1])
                        except:
                            print("Wrong value entered.\n")
                            continue
                        if number <= len(todo):
                            todo.pop(number-1)
                            print("Task removed.\n")
                        else:
                            print(f"You have only {len(todo)} items in your todo.\n")
                    else:
                        print("Wrong thing to remove\n")
                        continue
            else:
                print("Invalid menu.")
        else:
            print("Enter the input properly.\n")
        

if __name__ == "__main__":
    todo_list()