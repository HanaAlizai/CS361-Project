# Author: Hana Alizai
# Date: 7/17/23
# Milestone 1 Implementation


from expense import Expense
from budget import Budget
from pfms import PersonalFinanceManagementSystem


def show_terms_and_conditions():
    print("Welcome to the Personal Finance Management System!")
    print("Before getting started, please read and accept the terms and conditions.")
    print("By proceeding, you acknowledge that your data will be securely managed.")
    print("Terms and Conditions:")
    print("...")
    response = input("Do you accept the terms and conditions? (Yes/No): ")
    return response.lower() == "yes"


def main():
    if not show_terms_and_conditions():
        print("You must accept the terms and conditions to use the Personal Finance Management System.")
        return

    # Create personal finance management system object
    pfms = PersonalFinanceManagementSystem()

    expense_categories = ["Groceries", "Dining Out", "Shopping", "Transportation", "Utilities"]

    while True:
        print("===== Personal Finance Management System =====")
        print("1. Add Expense")
        print("2. Add Budget")
        print("3. Track Expenses")
        print("4. Track Budget Performance")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter the expense date: ")
            amount = float(input("Enter the expense amount: "))
            category = input(f"Enter the expense category ({', '.join(expense_categories)}): ")
            description = input("Enter the expense description: ")
            expense = Expense(date, amount, category, description)
            pfms.add_expense(expense)
            print("Expense added successfully!")

        elif choice == '2':
            category = input("Enter the budget category: ")
            limit = float(input("Enter the budget limit: $"))
            budget = Budget(category, limit)
            pfms.add_budget(budget)
            print("Budget added successfully!")

        elif choice == '3':
            category = input(f"Enter the category to track expenses ({', '.join(expense_categories)}): ")
            expenses = pfms.get_expenses_by_category(category)
            print(f"Expenses for category '{category}':")
            for expense in expenses:
                print(f"Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}")
            total_expenses = pfms.get_total_expenses()
            print(f"Total Expenses: {total_expenses}")

        elif choice == '4':
            pfms.track_budget_performance()

        elif choice == '5':
            print("Exiting the Personal Finance Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
