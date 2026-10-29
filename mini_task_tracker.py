import json

tasks = []


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("The tasks file could not be read. Starting with an empty list.")
        return []


def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    title = input("Enter the task title: ").strip()

    if title == "":
        print("Task title cannot be empty.")
    else:
        task = {"title": title, "done": False}
        tasks.append(task)
        save_tasks()
        print("Task added.")


def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks yet.")
    else:
        print("\nYour tasks:")
        for number in range(len(tasks)):
            if tasks[number]["done"] == True:
                status = "Done"
            else:
                status = "Pending"

            print(str(number + 1) + ". " + tasks[number]["title"] + " [" + status + "]")


def complete_task():
    view_tasks()

    if len(tasks) > 0:
        try:
            task_number = int(input("Enter the task number to complete: "))

            if task_number < 1 or task_number > len(tasks):
                print("That task number does not exist.")
            elif tasks[task_number - 1]["done"] == True:
                print("This task is already done.")
            else:
                tasks[task_number - 1]["done"] = True
                save_tasks()
                print("Task completed.")
        except ValueError:
            print("Please enter a valid whole number.")


def delete_task():
    view_tasks()

    if len(tasks) > 0:
        try:
            task_number = int(input("Enter the task number to delete: "))

            if task_number < 1 or task_number > len(tasks):
                print("That task number does not exist.")
            else:
                removed_task = tasks.pop(task_number - 1)
                save_tasks()
                print("Deleted task:", removed_task["title"])
        except ValueError:
            print("Please enter a valid whole number.")


tasks = load_tasks()

while True:
    print("\n--- TASK TRACKER ---")
    print("1. Add")
    print("2. View")
    print("3. Complete")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choice: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 5.")
