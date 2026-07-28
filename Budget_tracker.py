import csv
import os
import re

transactions = []
category_budgets = {}


def load_data():
    try:
        file = open("budget_data.csv", "r")
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if len(row) == 5:
                t = {
                    "date": row[0],
                    "type": row[1],
                    "category": row[2],
                    "description": row[3],
                    "amount": float(row[4])
                }
                transactions.append(t)
        file.close()
    except FileNotFoundError:
        pass

    if os.path.exists("budget_limits.csv"):
        try:
            with open("budget_limits.csv", "r") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) == 2:
                        category_budgets[row[0]] = float(row[1])
        except Exception:
            pass


def save_data():
    file = open("budget_data.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Date", "Type", "Category", "Description", "Amount"])
    for t in transactions:
        writer.writerow([t["date"], t["type"], t["category"], t["description"], t["amount"]])
    file.close()

    try:
        with open("budget_limits.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Limit"])
            for cat, limit in category_budgets.items():
                writer.writerow([cat, limit])
        print("Data saved successfully.")
    except Exception:
        print("Error saving budget limits.")


def add_transaction():
    print("\n--- Add Transaction ---")
    date = input("Enter date (YYYY-MM-DD): ")

    t_type = input("Enter type (Income/Expense): ").strip().capitalize()
    while t_type != "Income" and t_type != "Expense":
        print("Invalid type.")
        t_type = input("Enter type (Income/Expense): ").strip().capitalize()

    category = input("Enter category: ")
    description = input("Enter description: ")

    valid_amount = False
    amount = 0.0
    while not valid_amount:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                valid_amount = True
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    new_t = {
        "date": date,
        "type": t_type,
        "category": category,
        "description": description,
        "amount": amount
    }
    transactions.append(new_t)
    print("Transaction added.")

    if t_type == "Expense" and category in category_budgets:
        total = 0.0
        for item in transactions:
            if item["type"] == "Expense" and item["category"].lower() == category.lower():
                total = total + item["amount"]
        if total > category_budgets[category]:
            print(f"ALERT: You passed your budget for {category}! Spent: ${total:.2f}")


def view_transactions():
    print("\n--- All Transactions ---")
    if len(transactions) == 0:
        print("No transactions found.")
        return

    i = 0
    for t in transactions:
        print(
            f"[{i}] Date: {t['date']} | Type: {t['type']} | Category: {t['category']} | Desc: {t['description']} | Amount: ${t['amount']:.2f}")
        i = i + 1


def update_transaction():
    view_transactions()
    if len(transactions) == 0:
        return

    try:
        choice = int(input("\nEnter index to update: "))
        if choice >= 0 and choice < len(transactions):
            t = transactions[choice]

            new_date = input(f"New Date ({t['date']}): ")
            if new_date != "":
                t["date"] = new_date

            new_type = input(f"New Type ({t['type']}): ").strip().capitalize()
            if new_type in ["Income", "Expense"]:
                t["type"] = new_type

            new_cat = input(f"New Category ({t['category']}): ")
            if new_cat != "":
                t["category"] = new_cat

            new_desc = input(f"New Description ({t['description']}): ")
            if new_desc != "":
                t["description"] = new_desc

            new_amt = input(f"New Amount (${t['amount']}): ")
            if new_amt != "":
                try:
                    t["amount"] = float(new_amt)
                except ValueError:
                    print("Invalid amount. Old amount kept.")

            print("Transaction updated.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Enter a valid integer index.")

def delete_transaction():
    view_transactions()
    if len(transactions) == 0:
        return

    try:
        choice = int(input("\nEnter index to delete: "))
        if 0 <= choice < len(transactions):
            removed = transactions.pop(choice)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Enter a valid index.")


def calculate_balance():
    income = 0.0
    expense = 0.0

    for t in transactions:
        if t["type"] == "Income":
            income = income + t["amount"]
        elif t["type"] == "Expense":
            expense = expense + t["amount"]

    print("\n--- Balance ---")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expense:.2f}")
    print(f"Current Balance: ${income - expense:.2f}")


def category_summary():
    print("\n--- Category Spending ---")
    totals = {}

    for t in transactions:
        if t["type"] == "Expense":
            cat = t["category"]
            if cat in totals:
                totals[cat] = totals[cat] + t["amount"]
            else:
                totals[cat] = t["amount"]

    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")


def set_budgets():
    print("\n--- Set Budget Limit ---")
    cat = input("Enter expense category: ")
    try:
        limit = float(input(f"Enter limit for {cat}: $"))
        category_budgets[cat] = limit
        print("Budget set.")
    except ValueError:
        print("Invalid number.")

    print("\nBudget Status:")
    for b_cat, b_limit in category_budgets.items():
        spent = 0.0
        for t in transactions:
            if t["type"] == "Expense" and t["category"].lower() == b_cat.lower():
                spent = spent + t["amount"]

        status = "UNDER BUDGET"
        if spent > b_limit:
            status = "OVER BUDGET"
        print(f"{b_cat}: Spent ${spent:.2f} / Limit ${b_limit:.2f} [{status}]")


def monthly_summary():
    print("\n--- Monthly Summary ---")
    month_year = input("Enter Month and Year (YYYY-MM): ")

    m_income = 0.0
    m_expense = 0.0
    m_cats = {}

    for t in transactions:
        if t["date"].startswith(month_year):
            if t["type"] == "Income":
                m_income = m_income + t["amount"]
            elif t["type"] == "Expense":
                m_expense = m_expense + t["amount"]
                cat = t["category"]
                if cat in m_cats:
                    m_cats[cat] = m_cats[cat] + t["amount"]
                else:
                    m_cats[cat] = t["amount"]

    print(f"\nSummary for {month_year}:")
    print(f"Income: ${m_income:.2f}")
    print(f"Expenses: ${m_expense:.2f}")
    print(f"Net: ${m_income - m_expense:.2f}")
    for c, amnt in m_cats.items():
        print(f"  {c}: ${amnt:.2f}")


def ai_validated_date_input(prompt):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    while True:
        val = input(prompt).strip()
        if pattern.match(val):
            return val
        print("[AI Improved Check] Invalid date format. Please use YYYY-MM-DD.")


def ai_view_transactions_formatted():
    print("\n" + "=" * 70)
    print(f"{'ID':<4} | {'Date':<10} | {'Type':<8} | {'Category':<12} | {'Amount':<9} | {'Description'}")
    print("=" * 70)
    if not transactions:
        print("No transactions to display.")
        return
    for idx, t in enumerate(transactions):
        print(
            f"{idx:<4} | {t['date']:<10} | {t['type']:<8} | {t['category']:<12} | ${t['amount']:<8.2f} | {t['description']}")
    print("=" * 70)


def main():
    load_data()
    running = True

    while running:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View All Transactions (Basic)")
        print("5. View All Transactions (AI Formatted Table)")
        print("6. Calculate Current Balance")
        print("7. Category Spending Summary")
        print("8. Set and Check Budget Limits")
        print("9. Monthly Summary Report")
        print("10. Save and Exit")

        choice = input("Select an option (1-10): ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            update_transaction()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            ai_view_transactions_formatted()
        elif choice == "6":
            calculate_balance()
        elif choice == "7":
            category_summary()
        elif choice == "8":
            set_budgets()
        elif choice == "9":
            monthly_summary()
        elif choice == "10":
            save_data()
            running = False
        else:
            print("Invalid menu option.")


if __name__ == "__main__":
    main()