#Welcome message
print("Welcome to the Personal Finance Tracker!")

#Adding an expense with the add_expense function
def add_expense(data):

    while True:

#setting up prompts for user input of expense description, category, and amount
            expense = input("Enter expense description (enter 'exit' to quit): ")
            if expense.lower() == 'exit':
                return False

            category = input("Enter category: ")
            amount_str = input("Enter amount: ")
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be greater than zero. Try again.")
                    continue

                expense_record = {
                    "description": expense,
                    "category": category,
                    "amount": amount,
                }
                data.append(expense_record)

                print(f"\nCategory: {category}")
                print(f" - {expense}: ${amount:.2f}")
                print("Expense added successfully!")

                return
#exception for a value error indicating that the user will need to input a valid number
            except ValueError:
                print("Invalid value! Please enter a valid number.")
#finally block that indicates that the expenses process is complete
            finally:
                print("Expenses process complete.")

#Viewing an expense with the view_expense function
def view_expenses(data):
    if not data:
        print("No expenses were added yet!")
        return
    expenses_by_category = {}
    for expense in data:
        category = expense["category"]
        if category not in expenses_by_category:
            expenses_by_category[category] = []
        expenses_by_category[category].append(expense)
#organizing viewing of expenses, ensuring the proper format is printed based on user input values
    try:
        for category, expenses_in_category in expenses_by_category.items():
            print(f"\n Category: {category}")

            for expense in expenses_in_category:
                print(f" - {expense['description']}: ${expense['amount']:.2f}")
#exception for a key error when information from the user is missing
    except KeyError:
        print(f"Error: no expenses were found. Try again and ensure all inputs are valid.")

#Viewing the summary with the view_summary function
def view_summary(data):
    if not data:
        print("\nNo expenses have been added yet.")
        return
    try:
        category_totals = {}

        for expense in data:
            category = expense["category"]
            amount = expense["amount"]
            category_totals[category] = category_totals.get(category, 0) + amount
#Printing the summary format
        print("\nSummary:")

        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
#exception for key error. Indicating the user might have missed inputting some information
    except KeyError:
        print(f"Error: Some records are missing, the key cannot be used. Try again and ensure all inputs are valid.")

#main() function for menu logic
def main():

#menu setup that prints the options
    expenses = []
    print ("What would you like to do?")

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

#taking user input for menu choice
        choice = input("Enter your choice (1-4): ")
#conditional statements that call the appropriate functions to display category, description, and expense values
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_summary(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#ensuring the program runs through main()
if __name__ == '__main__':
    main()





