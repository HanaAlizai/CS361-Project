# Author: Hana Alizai
# Date: 7/17/23
# Milestone 1 Implementation
class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
