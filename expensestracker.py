import json

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        """Save expenses to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        """Add a new expense."""
        try:
            amount = float(amount)  
            self.expenses.append({"amount": amount, "category": category, "description": description})
            self.save_expenses()
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. Amount: Rs{expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def analyze_expenses(self):
        """Provide a summary of expenses by category."""
        summary = {}
        for expense in self.expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]
        
        print("Expense Summary by Category:")
        for category, total in summary.items():
            print(f"{category}: Rs{total:.2f}")

    def run(self):
        """Main loop for user interaction."""
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Analyze Expenses")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                amount = input("Enter amount spent: ")
                category = input("Enter category (e.g., food, transport, bills): ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.analyze_expenses()
            elif choice == "4":
                print("Exiting Expense Tracker. Thank you! visit Again")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
