"""
Task 4: To-Do List Manager
"""

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
                print("Task removed.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
