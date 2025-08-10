"============EXPENSE TRACKER============"

Expenses = []

def add_expense(expense, category):
    """Add an expense to the tracker."""
    Expenses.append({"expense": expense, "category": category})
    print(f"Expense '{expense}' in category '{category}' added.")

def view_expenses():
    """View all expenses in the tracker."""
    if not Expenses:
        print("No expenses recorded.")
        return
    print("Expenses:")
    for i, expense in enumerate(Expenses, start=1):
        print(f"{i}. {expense['expense']} - Category: {expense['category']}")


def remove_expense(expense):
    """Remove an expense from the tracker."""
    for i, exp in enumerate(Expenses):
        if exp["expense"] == expense:
            del Expenses[i]
            print(f"Expense '{expense}' removed.")
            return
    print(f"Expense '{expense}' not found in the tracker.")            


def total_expenses():
    """Calculate the total expenses."""
    total = sum(exp["expense"] for exp in Expenses)
    print(f"Total expenses: {total}")    

def highest_expense():
    """Find the highest expense."""
    if not Expenses:
        print("No expenses recorded.")
        return
    highest = max(Expenses, key=lambda x: x["expense"])
    print(f"Highest expense: {highest['expense']} in category '{highest['category']}'")


def menu():
    """Display the menu and handle user input."""
    
    print("\n----Expense Tracker Menu----")
    print("1: Add Expense")
    print("2: View Expenses")
    print("3: Remove Expense")
    print("4: Total Expenses")
    print("5: Highest Expense")
    print("6: Exit")
while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            expense = float(input("Enter the expense amount: "))
            category = input("Enter the category of the expense: ")
            add_expense(expense, category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense = input("Enter the expense to remove: ")
            remove_expense(expense)
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            highest_expense()
        elif choice == "6":
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")        