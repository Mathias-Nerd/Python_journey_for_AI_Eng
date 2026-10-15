#Mathias-Nerd
#Week 4: Question 4 OOP version
#Build a small command-line to-do list. The user should be able to add a task, view all tasks, remove a task, or quit the program.
# Display a menu repeatedly until the user chooses to quit. Number tasks when displaying them so the user can select which task to remove.

class ToDo:
    def __init__(self):
        self.storage = []
        while True:
            user_input = input("Menu choices: add, view, remove, quit: ").strip().lower()
            if user_input == "add":
                self.add()
            elif user_input == "view":
                self.view()
            elif user_input == "remove":
                self.remove()
            elif user_input == "quit":
                break
            else:
                print("Invalid choice!")


    def add(self):
        self.storage.append(input("Add item: "))

    def remove(self):
        if self.storage:
            print("Enter the task you will like to remove [e.g. 1,2,3]: ")
            item = int(input())
            if item <= len(self.storage):
                self.storage.pop(item - 1)
            else:
                print(f"You only have {len(self.storage)} items in you todo." if len(self.storage) > 1 else f"You only have {len(self.storage)} item in you todo.") 
        else:
            print("There is no task to remove.")

    def view(self):
        if not self.storage:
            print("Your todo list is empty.")
        for index, task in enumerate(self.storage, start=1):
            print(f"{index}. {task}")

    
todo = ToDo()

name = "Mathias"
isinstance(name, str)