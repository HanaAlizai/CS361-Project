# Author: Hana Alizai
# Date: 7/17/23
# Milestone 1 Implementation

import tkinter as tk
from tkinter import messagebox, ttk
from expense import Expense
from budget import Budget
from pfms import PersonalFinanceManagementSystem, Goal, Income, Reminder


class TermsAndConditionsPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Terms and Conditions")
        self.geometry("400x300")
        self.resizable(False, False)

        self.terms_text = """
        By clicking Accept, you agree to our Privacy Policy.
        """

        self.terms_text = tk.Label(self, text=self.terms_text, justify="left")
        self.terms_text.pack(padx=10, pady=10)

        self.agree_var = tk.BooleanVar()
        self.agree_checkbutton = tk.Checkbutton(self, text="I Agree to the Terms and Conditions",
                                                variable=self.agree_var)
        self.agree_checkbutton.pack(pady=10)

        self.continue_button = tk.Button(self, text="Continue", command=self.continue_to_app)
        self.continue_button.pack(pady=10)

    def continue_to_app(self):
        if self.agree_var.get():
            self.destroy()
            app = LoginPage()
            app.mainloop()
        else:
            messagebox.showwarning("Terms and Conditions", "Please agree to the terms and conditions.")


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x150")
        self.resizable(False, False)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Perform login authentication logic here
        # username: "admin" and password: "password" are valid
        if username == "admin" and password == "password":
            self.destroy()
            app = PersonalFinanceManagementSystemGUI()
            app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")


class PersonalFinanceManagementSystemGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Management System")

        # Create personal finance management system object
        self.pfms = PersonalFinanceManagementSystem()

        self.undo_stack = []
        self.redo_stack = []

        self.expense_categories = ["Groceries", "Dining Out", "Shopping", "Transportation", "Utilities"]

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("TFrame", background="#F0F0F0")
        self.style.configure("TFrame", background="#90EE90")

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        sandbox_mode = tk.BooleanVar()
        sandbox_checkbox = tk.Checkbutton(main_frame, text="Sandbox Mode", variable=sandbox_mode)
        sandbox_checkbox.pack()

        # Add Expense section
        expense_frame = tk.LabelFrame(main_frame, text="Add Expense")
        expense_frame.pack(fill="both", expand=True, padx=10, pady=10)

        expense_date_label = tk.Label(expense_frame, text="Date:")
        expense_date_label.grid(row=0, column=0, sticky="w")
        self.expense_date_entry = tk.Entry(expense_frame)
        self.expense_date_entry.grid(row=0, column=1)

        expense_amount_label = tk.Label(expense_frame, text="Amount:")
        expense_amount_label.grid(row=1, column=0, sticky="w")
        self.expense_amount_entry = tk.Entry(expense_frame)
        self.expense_amount_entry.grid(row=1, column=1)

        expense_category_label = tk.Label(expense_frame, text="Category:")
        expense_category_label.grid(row=2, column=0, sticky="w")
        self.expense_category_variable = tk.StringVar()
        self.expense_category_variable.set(self.expense_categories[0])
        self.expense_category_optionmenu = tk.OptionMenu(expense_frame, self.expense_category_variable,
                                                         *self.expense_categories)
        self.expense_category_optionmenu.grid(row=2, column=1)

        expense_description_label = tk.Label(expense_frame, text="Description:")
        expense_description_label.grid(row=3, column=0, sticky="w")
        self.expense_description_entry = tk.Entry(expense_frame)
        self.expense_description_entry.grid(row=3, column=1)

        add_expense_button = tk.Button(expense_frame, text="Add Expense", command=self.add_expense)
        add_expense_button.grid(row=4, columnspan=2)

        undo_button = tk.Button(expense_frame, text="Undo", command=self.undo)
        undo_button.grid(row=5, column=0, padx=5, pady=5)

        redo_button = tk.Button(expense_frame, text="Redo", command=self.redo)
        redo_button.grid(row=5, column=1, padx=5, pady=5)

        # Track Expenses section
        track_expenses_frame = tk.LabelFrame(main_frame, text="Track Expenses")
        track_expenses_frame.pack(fill="both", expand=True, padx=10, pady=10)

        track_expenses_category_label = tk.Label(track_expenses_frame, text="Category:")
        track_expenses_category_label.grid(row=0, column=0, sticky="w")
        self.track_expenses_category_variable = tk.StringVar()
        self.track_expenses_category_variable.set(self.expense_categories[0])
        self.track_expenses_category_optionmenu = tk.OptionMenu(track_expenses_frame,
                                                                self.track_expenses_category_variable,
                                                                *self.expense_categories)
        self.track_expenses_category_optionmenu.grid(row=0, column=1)

        track_expenses_button = tk.Button(track_expenses_frame, text="Track Expenses", command=self.track_expenses)
        track_expenses_button.grid(row=1, columnspan=2)

        undo_button = tk.Button(track_expenses_frame, text="Undo", command=self.undo)
        undo_button.grid(row=5, column=0, padx=5, pady=5)

        redo_button = tk.Button(track_expenses_frame, text="Redo", command=self.redo)
        redo_button.grid(row=5, column=1, padx=5, pady=5)

        # Add Income section
        income_frame = tk.LabelFrame(main_frame, text="Add Income")
        income_frame.pack(fill="both", expand=True, padx=10, pady=10)

        income_source_label = tk.Label(income_frame, text="Source:")
        income_source_label.grid(row=0, column=0, sticky="w")
        self.income_source_entry = tk.Entry(income_frame)
        self.income_source_entry.grid(row=0, column=1)

        income_amount_label = tk.Label(income_frame, text="Amount:")
        income_amount_label.grid(row=1, column=0, sticky="w")
        self.income_amount_entry = tk.Entry(income_frame)
        self.income_amount_entry.grid(row=1, column=1)

        add_income_button = tk.Button(income_frame, text="Add Income", command=self.add_income)
        add_income_button.grid(row=2, columnspan=2)

        undo_button = tk.Button(income_frame, text="Undo", command=self.undo)
        undo_button.grid(row=5, column=0, padx=5, pady=5)

        redo_button = tk.Button(income_frame, text="Redo", command=self.redo)
        redo_button.grid(row=5, column=1, padx=5, pady=5)
        # Add Goal section
        goal_frame = tk.LabelFrame(main_frame, text="Add Goal")
        goal_frame.pack(fill="both", expand=True, padx=10, pady=10)

        goal_name_label = tk.Label(goal_frame, text="Name:")
        goal_name_label.grid(row=0, column=0, sticky="w")
        self.goal_name_entry = tk.Entry(goal_frame)
        self.goal_name_entry.grid(row=0, column=1)

        goal_target_label = tk.Label(goal_frame, text="Target Amount:")
        goal_target_label.grid(row=1, column=0, sticky="w")
        self.goal_target_entry = tk.Entry(goal_frame)
        self.goal_target_entry.grid(row=1, column=1)

        add_goal_button = tk.Button(goal_frame, text="Add Goal", command=self.add_goal)
        add_goal_button.grid(row=2, columnspan=2)

        undo_button = tk.Button(goal_frame, text="Undo", command=self.undo)
        undo_button.grid(row=5, column=0, padx=5, pady=5)

        redo_button = tk.Button(goal_frame, text="Redo", command=self.redo)
        redo_button.grid(row=5, column=1, padx=5, pady=5)

        # Add Reminder section
        reminder_frame = tk.LabelFrame(main_frame, text="Add Reminder")
        reminder_frame.pack(fill="both", expand=True, padx=10, pady=10)

        expense_frame.pack(side="left")
        track_expenses_frame.pack(side="bottom")
        income_frame.pack(side="left")
        goal_frame.pack(side="bottom")
        reminder_frame.pack(side="right")


        reminder_description_label = tk.Label(reminder_frame, text="Description:")
        reminder_description_label.grid(row=0, column=0, sticky="w")
        self.reminder_description_entry = tk.Entry(reminder_frame)
        self.reminder_description_entry.grid(row=0, column=1)

        reminder_due_date_label = tk.Label(reminder_frame, text="Due Date:")
        reminder_due_date_label.grid(row=1, column=0, sticky="w")
        self.reminder_due_date_entry = tk.Entry(reminder_frame)
        self.reminder_due_date_entry.grid(row=1, column=1)

        add_reminder_button = tk.Button(reminder_frame, text="Add Reminder", command=self.add_reminder)
        add_reminder_button.grid(row=2, columnspan=2)

    def add_expense(self):
        date = self.expense_date_entry.get()
        amount = float(self.expense_amount_entry.get())
        category = self.expense_category_variable.get()
        description = self.expense_description_entry.get()

        if date and category:
            expense = Expense(date, amount, category, description)
            self.pfms.add_expense(expense)
            messagebox.showinfo("Expense Added", "Expense added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a date and select a category.")

        if amount > 1000:
            messagebox.showwarning("Warning",
                                   "The expense amount is quite high. Consider reviewing your budget before proceeding.")

        self.undo_stack.append(('add_expense', expense))
        # Clear the redo stack since a new change was made
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            # Get the last change from the undo stack
            action, data = self.undo_stack.pop()

            if action == 'add_expense':
                # Remove the expense from the personal finance management system
                self.pfms.remove_expense(data)
                # Add the change to the redo stack
                self.redo_stack.append(('add_expense', data))

    def redo(self):
        if self.redo_stack:
            # Get the last change from the redo stack
            action, data = self.redo_stack.pop()

            if action == 'add_expense':
                # Add the expense back to the personal finance management system
                self.pfms.add_expense(data)
                # Add the change to the undo stack
                self.undo_stack.append(('add_expense', data))

    def track_expenses(self):
        category = self.track_expenses_category_variable.get()

        if category:
            expenses = self.pfms.get_expenses_by_category(category)
            total_expenses = self.pfms.get_total_expenses()

            messagebox.showinfo(
                "Track Expenses",
                f"Expenses for category '{category}':\n\n"
                f"Total Expenses: {total_expenses}"
            )
        else:
            messagebox.showerror("Error", "Please select a category.")

    def add_income(self):
        source = self.income_source_entry.get()
        amount = float(self.income_amount_entry.get())

        if source and amount:
            income = Income(source, amount)
            self.pfms.add_income(income)
            messagebox.showinfo("Income Added", "Income added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a source and amount for the income.")
        self.undo_stack.append(('add_income', income))
        # Clear the redo stack since a new change was made
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            # Get the last change from the undo stack
            action, data = self.undo_stack.pop()

            if action == 'add_income':
                # Remove the expense from the personal finance management system
                self.pfms.remove_expense(data)
                # Add the change to the redo stack
                self.redo_stack.append(('add_income', data))

    def redo(self):
        if self.redo_stack:
            # Get the last change from the redo stack
            action, data = self.redo_stack.pop()

            if action == 'add_income':
                # Add the expense back to the personal finance management system
                self.pfms.add_income(data)
                # Add the change to the undo stack
                self.undo_stack.append(('add_income', data))

    def add_goal(self):
        name = self.goal_name_entry.get()
        target_amount = float(self.goal_target_entry.get())

        if name and target_amount:
            goal = Goal(name, target_amount)
            self.pfms.add_goal(goal)
            messagebox.showinfo("Goal Added", "Goal added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a name and target amount for the goal.")

    def add_reminder(self):
        description = self.reminder_description_entry.get()
        due_date = self.reminder_due_date_entry.get()

        if description and due_date:
            reminder = Reminder(description, due_date)
            self.pfms.add_reminder(reminder)
            messagebox.showinfo("Reminder Added", "Reminder added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a description and due date for the reminder.")

        self.style.configure("Accent.TLabelframe", background="#90EE90")
        self.style.map("Accent.TLabelframe",
                       background=[("active", "#90EE90"), ("disabled", "#FFECB3")])

        self.style.configure("TButton", background="#FFC109", foreground="#000000")
        self.style.map("TButton",
                       background=[("active", "#90EE90"), ("disabled", "#FFECB3")])

        self.configure(background="#90EE90")


if __name__ == "__main__":
    terms_page = TermsAndConditionsPage()
    terms_page.mainloop()
