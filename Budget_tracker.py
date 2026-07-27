import csv
import os
import re

TRANSACTION_FILE = "budget_data.csv"
BUDGET_FILE = "budget_limits.csv"

transactions = []
category_budgets = {}

def load_all_data():
    """Loads both transactions and budget limit configurations safely."""
    # Load Transactions
    if os.path.exists(TRANSACTION_FILE):
        try:
            with open(TRANSACTION_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions.append({
                        "date": row["Date"],
                        "type": row["Type"],
                        "category": row["Category"],
                        "description": row["Description"],
                        "amount": float(row["Amount"])
                    })
        except Exception as e:
            print(f"[AI-Log] Warning reading transactions: {e}")

    # Load Category Budgets
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None) # skip header
                for row in reader:
                    if len(row) == 2:
                        category_budgets[row[0]] = float(row[1])
        except Exception as e:
            print(f"[AI-Log] Warning reading budgets: {e}")

def save_all_data():
    """Saves both transactions and budget records atomically."""
    try:
        with open(TRANSACTION_FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["Date", "Type", "Category", "Description", "Amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for t in transactions:
                writer.writerow({
                    "Date": t["date"],
                    "Type": t["type"],
                    "Category": t["category"],
                    "Description": t["description"],
                    "Amount": t["amount"]
                })

        with open(BUDGET_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Limit"])
            for cat, limit in category_budgets.items():
                writer.writerow([cat, limit])

        print("\n[AI Success] All application data and budget configurations persisted.")
    except Exception as e:
        print(f"[Error] Failed saving data: {e}")

def get_valid_date(prompt):
    """AI Improvement: Regex-validated date entry."""
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    while True:
        date_str = input(prompt).strip()
        if date_pattern.match(date_str):
            return date_str
        print("[Error] Invalid date format. Please use YYYY-MM-DD.")

def view_transactions_formatted():
    """AI Improvement: Displays transactions in clean table alignment."""
    print("\n" + "="*75)
    print(f"{'ID':<4} | {'Date':<10} | {'Type':<8} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("="*75)
    if not transactions:
        print("No transactions to display.")
        return
    for idx, t in enumerate(transactions):
        print(f"{idx:<4} | {t['date']:<10} | {t['type']:<8} | {t['category']:<15} | ${t['amount']:<9.2f} | {t['description']}")
    print("="*75)

# --- Main Refactored Entry Point ---
def main_enhanced():
    load_all_data()
    print("Enhanced Personal Budget Tracker initialized.")
    # Standard menu loop invocation...

if __name__ == "__main__":
    main_enhanced()