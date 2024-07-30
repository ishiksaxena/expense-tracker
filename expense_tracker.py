import csv
import datetime

# File to store the expenses
FILENAME = "expenses.csv"

# Function to initialize the CSV file
def initialize_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount"])
    except FileExistsError:
        pass  # File already exists

# Function to add a new expense
def add_expense(description, amount):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])

# Function to view all expenses
def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            print("Date\t\t\tDescription\tAmount")
            print("-------------------------------------------------")
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to display the menu and handle user choices
def menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(description, amount)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        if _name_ == "_main_":
            initialize_file()
            menu()