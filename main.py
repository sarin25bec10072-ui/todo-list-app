tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == "3":
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted!")
        else:
            print("Invalid number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")