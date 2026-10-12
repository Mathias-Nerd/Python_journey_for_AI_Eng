#Mathias-Nerd
#Week 4: Question 4
#Build a small command-line to-do list. The user should be able to add a task, view all tasks, remove a task, or quit the program.
# Display a menu repeatedly until the user chooses to quit. Number tasks when displaying them so the user can select which task to remove.
todo = []
while True:
    user_input = input("Menu choices: add, view, remove, quit: ").strip().lower()
    if user_input == "add":
        todo.append(input("Add item: "))
    elif user_input == "remove":
        if todo:
            print("Enter the task you will like to remove [e.g. 1,2,3]: ")
            item = int(input())
            if item <= len(todo):
                todo.pop(item - 1)
            else:
                print(f"You only have {len(todo)} items in you todo." if len(todo) > 1 else f"You only have {len(todo)} item in you todo.") 
        else:
            print("There is no task to remove.")

    elif user_input == "view":
        if not todo:
            print("Your todo list is empty.")
        else:
            for index, task in enumerate(todo, start=1):
                print(f"{index}. {task}")
    elif user_input == "quit":
        break
    else:
        print("Invalid choice!")