"""A simple To-Do List application in Python that allows users to add,
 view, and remove tasks."""

tasks=[]


while True:
    print("----To-Do List App-----")
    print("\n 1: Add Task \n 2: View Tasks \n 3: Remove Task \n 4: Exit")

    choice=input("Enter your choice:")
    if choice == "1":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")

    elif choice == "2":
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")

    elif choice == "3":
        task= input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed.")

        else:
            print(f"Task '{task}' not found in the list.")


    elif choice == "4":
        print("Exiting the To-Do List App.")
        break
    else:
        print("Invalid choice. Please try again.")                   