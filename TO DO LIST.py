def main():
    tasks=[]
    def display_menu():
        print("MENU")
        print("1. Add Task")
        print("2. DISPLAY")
        print("3. Mark Task as Done")
        print("4. Exit")
    while True:
        display_menu()
        choice=int(input("Enter your choice:"))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            display(tasks)
        elif choice == 3:
            mark_done(tasks)
        elif choice == 4:
            exit_list()
        else:
            print("Invalid choice. Please select a valid option.")

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")

def display(tasks):
    print("TO DO LIST")
    for i in tasks:
        print(i)

def mark_done(tasks):
    task_index=int(input("Enter task number:"))
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(removed_task,"\nmarked as done and removed.")
    else:
        print("Invalid task index.")

def exit_list():
    print("Exiting the To-Do List.")
    exit()

main()