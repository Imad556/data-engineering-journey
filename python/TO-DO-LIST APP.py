"""
A simple To-Do List application in Python that allows users to add, view, and remove tasks.
"""

tasks = []  # List to store tasks


while True:
    # Display the menu
    print("----To-Do List App-----")
    print("\n 1: Add Task \n 2: View Tasks \n 3: Remove Task \n 4: Exit")

    # Get user input for menu choice
    choice = input("Enter your choice:")

    if choice == "1":
        # Add a new task
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")

    elif choice == "2":
        # View all tasks
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks available.")

    elif choice == "3":
        # Remove a task by name
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found in the list.")

    elif choice == "4":
        # Exit the app
        print("Exiting the To-Do List App.")
        break
    else:
        # Handle invalid menu choices
        print("Invalid choice. Please try again.")