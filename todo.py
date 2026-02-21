import os
import json

FILENAME= "tasks.json"

def load_tasks():
       tasks=load_tasks
       if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
   task = input("Enter new task: ")
   tasks.append(task)
   print("Task added successfully!\n")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        number = int(input("Enter task number to remove: "))
        removed = tasks.pop(number - 1)
        print(f"Removed: {removed}\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")

def main():
 tasks = load_tasks()

 while True:
    print("===== TO-DO LIST =====")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        display_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break
    else:
     print("Invalid choice.\n")

    input("Press Enter to continue")


if __name__ == "__main__":
    main()



