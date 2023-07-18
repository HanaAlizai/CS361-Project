# Author: Hana Alizai
# Date: 7/17/23
# Milestone 1 Implementation
class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description


class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)


class PersonalFinanceManagementSystem:
    def __init__(self):
        self.expenses = []
        self.budgets = []
        self.goals = []
        self.incomes = []
        self.reminders = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_budget(self, budget):
        self.budgets.append(budget)

    def add_goal(self, goal):
        self.goals.append(goal)

    def add_income(self, income):
        self.incomes.append(income)

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def track_budget_performance(self):
        for budget in self.budgets:
            total_expenses = budget.get_total_expenses()
            if total_expenses > budget.limit:
                print(f"Budget for {budget.category} exceeded. Limit: {budget.limit}. Total Expenses: {total_expenses}")
            else:
                print(f"Budget for {budget.category} is within the limit.")

    def get_total_income(self):
        return sum(income.amount for income in self.incomes)

    def add_goal_progress(self, goal_name, progress_amount):
        for goal in self.goals:
            if goal.name == goal_name:
                goal.add_progress(progress_amount)
                break

    def set_reminder(self, reminder):
        self.reminders.append(reminder)

    def remove_expense(self, expense):
        if expense in self.expenses:
            self.expenses.remove(expense)


class Goal:
    def __init__(self, name, target_amount):
        self.name = name
        self.target_amount = target_amount
        self.progress = 0

    def add_progress(self, amount):
        self.progress += amount

    def is_completed(self):
        return self.progress >= self.target_amount


class Income:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount


class Reminder:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date


# Create expense, budget, goal, income, and reminder objects
expense1 = Expense("2023-07-15", 50.0, "Groceries", "Weekly grocery shopping")
expense2 = Expense("2023-07-16", 30.0, "Dining Out", "Dinner with friends")
budget1 = Budget("Groceries", 200.0)
budget2 = Budget("Dining Out", 100.0)
goal1 = Goal("Vacation", 1000.0)
income1 = Income("Salary", 3000.0)
reminder1 = Reminder("Pay utility bill", "2023-07-20")

# Create personal finance management system object
pfms = PersonalFinanceManagementSystem()

# Add expenses, budgets, goals, incomes, and reminders to the system
pfms.add_expense(expense1)
pfms.add_expense(expense2)
pfms.add_budget(budget1)
pfms.add_budget(budget2)
pfms.add_goal(goal1)
pfms.add_income(income1)
pfms.set_reminder(reminder1)

# Get expenses by category and print total expenses
grocery_expenses = pfms.get_expenses_by_category("Groceries")
print("Grocery Expenses:")
for expense in grocery_expenses:
    print(expense.date, expense.amount, expense.description)
print("Total Expenses:", pfms.get_total_expenses())

# Track budget performance
pfms.track_budget_performance()

# Print total income
print("Total Income:", pfms.get_total_income())

# Add progress to a goal
pfms.add_goal_progress("Vacation", 500.0)

# Check if a goal is completed
vacation_goal = pfms.goals[0]
if vacation_goal.is_completed():
    print("Goal 'Vacation' is completed.")
else:
    print("Goal 'Vacation' is not completed.")

# Print reminders
print("Reminders:")
for reminder in pfms.reminders:
    print(reminder.description, reminder.due_date)
