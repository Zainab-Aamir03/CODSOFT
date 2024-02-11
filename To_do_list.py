

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task + "\n")
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")

def remove_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    show_tasks()

    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task.strip()}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

# Modify the main function to call remove_task without arguments
def main():
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
