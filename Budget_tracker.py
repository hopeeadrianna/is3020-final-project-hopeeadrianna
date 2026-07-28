import csv

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
        print("No saved data file found.")


def save_data():
    try:
        file = open("budget_data.csv", "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["Date", "Type", "Category", "Description", "Amount"])
        for t in transactions:
            writer.writerow([t["date"], t["type"], t["category"], t["description"], t["amount"]])
        file.close()
        print("Data saved successfully!")
    except Exception:
        print("Error saving data.")


def add_transaction():
    print("\n--- Add Transaction ---")
    date = input("Enter date (YYYY-MM-DD): ")

    t_type = input("Enter type (Income or Expense): ").strip().capitalize()
    while t_type != "Income" and t_type != "Expense":
        print("Invalid choice.")
        t_type = input("Enter type (Income or Expense): ").strip().capitalize()

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
                print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

    t = {
        "date": date,
        "type": t_type,
        "category": category,
        "description": description,
        "amount": amount
    }
    transactions.append(t)
    print("Transaction added!")

    if t_type == "Expense" and category in category_budgets:
        total = 0.0
        for item in transactions:
            if item["type"] == "Expense" and item["category"].lower() == category.lower():
                total = total + item["amount"]
        if total > category_budgets[category]:
            print(f"ALERT: You passed your budget limit for {category}!")


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
        if 0 <= choice < len(transactions):
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
        print("Please enter a valid index number.")


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
        print("Please enter a valid index number.")


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
        limit = float(input(f"Enter spending limit for {cat}: $"))
        category_budgets[cat] = limit
        print("Budget set.")
    except ValueError:
        print("Invalid amount.")

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


def main():
    load_data()
    running = True

    while running:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View All Transactions")
        print("5. Calculate Current Balance")
        print("6. Category Spending Summary")
        print("7. Set and Check Budget Limits")
        print("8. Monthly Summary Report")
        print("9. Save and Exit")

        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            update_transaction()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            calculate_balance()
        elif choice == "6":
            category_summary()
        elif choice == "7":
            set_budgets()
        elif choice == "8":
            monthly_summary()
        elif choice == "9":
            save_data()
            running = False
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()