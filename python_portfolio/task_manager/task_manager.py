# task_manager.py

import datetime

# --- رنگ‌ها ---
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

TASK_FILE = "tasks.txt"
CATEGORIES = ["Work", "Personal", "Important"]

# --- افزودن Task ---
def add_task():
    title = input(CYAN + "Enter task title: " + RESET)
    print("Select category:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    try:
        cat_choice = int(input(CYAN + "Category number: " + RESET))
        if 1 <= cat_choice <= len(CATEGORIES):
            category = CATEGORIES[cat_choice - 1]
        else:
            print(RED + "Invalid category. Defaulting to Personal." + RESET)
            category = "Personal"
    except ValueError:
        print(RED + "Invalid input. Defaulting to Personal." + RESET)
        category = "Personal"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(TASK_FILE, "a") as file:
        file.write(f"{title}|{category}|{timestamp}\n")
    print(GREEN + f"Task '{title}' added under '{category}'!" + RESET)

# --- نمایش همه Task‌ها ---
def show_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print(YELLOW + "No tasks found." + RESET)
                return
            print(BLUE + "\n--- Task List ---" + RESET)
            for idx, task in enumerate(tasks, 1):
                title, category, timestamp = task.strip().split("|")
                color = GREEN if category == "Work" else CYAN
                if category == "Important":
                    color = RED
                print(f"{idx}. {color}{title} [{category}] - {timestamp}{RESET}")
    except FileNotFoundError:
        print(YELLOW + "No tasks found." + RESET)

# --- حذف Task ---
def delete_task():
    show_tasks()
    try:
        choice = int(input(CYAN + "Enter task number to delete: " + RESET))
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            with open(TASK_FILE, "w") as file:
                file.writelines(tasks)
            print(GREEN + f"Task '{removed.strip().split('|')[0]}' deleted!" + RESET)
        else:
            print(RED + "Invalid task number." + RESET)
    except (ValueError, FileNotFoundError):
        print(RED + "Error deleting task." + RESET)

# --- جستجوی Task ---
def search_task():
    keyword = input(CYAN + "Enter keyword to search: " + RESET)
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            found = [t.strip() for t in tasks if keyword.lower() in t.lower()]
            if found:
                print(BLUE + "\n--- Search Results ---" + RESET)
                for t in found:
                    title, category, timestamp = t.split("|")
                    color = GREEN if category == "Work" else CYAN
                    if category == "Important":
                        color = RED
                    print(f"- {color}{title} [{category}] - {timestamp}{RESET}")
            else:
                print(YELLOW + "No matching tasks found." + RESET)
    except FileNotFoundError:
        print(YELLOW + "No tasks found." + RESET)

# --- منوی اصلی ---
def main():
    while True:
        print(MAGENTA + "\n--- Professional Task Manager ---" + RESET)
        print(BLUE + "1. Add Task" + RESET)
        print(BLUE + "2. Show Tasks" + RESET)
        print(BLUE + "3. Delete Task" + RESET)

        print(BLUE + "4. Search Task" + RESET)
        print(BLUE + "5. Exit" + RESET)
        choice = input(CYAN + "Choose an option: " + RESET)

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print(GREEN + "Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid option." + RESET)

if __name__ == "__main__":
    main()
