# IS 3020 Final Project

## Student and Project Information

- Student name: Hope McDowell
- GitHub username: hopeeadrianna 
- Project title: Personal Budget Tracker 
- Application purpose: To help users track their money. It keeps track of spending and income, organizes money by category, warns users when they spend too much, and saves all data to files.

## How to Run the Application

Required Python Version
Python 3.14 

Required Files
Put these files in the same project folder:
budget_tracker.py (The main Python code file)
budget_data.csv (File that saves your transactions)
budget_limits.csv (File that saves your budget limits)

Exact Steps to Run in PyCharm
Open PyCharm.
Click File > Open, and select your project folder.
Make sure Python is set up under Settings > Project > Python Interpreter.
Right-click budget_tracker.py on the left side menu.
Click Run 'budget_tracker'.
Use the menu in the bottom window by typing numbers 1 through 10.

## Major Features

1. Add Transaction: Type in new money coming in (Income) or going out (Expense). Includes automated warning alerts if you go over budget.
2. Update Transaction: Pick an existing transaction and change its details.
3. Delete Transaction: Remove a transaction from your list.
4. View All Transactions (Basic): See a simple list of all your money entries.
5. View All Transactions (AI Formatted Table): See a clean, neat table of all your entries.
6. Calculate Current Balance: Shows total income, total expenses, and how much money you have left.
7. Category Spending Summary: Shows how much money you spent in each category (like Food or Gas).
8. Set and Check Budget Limits: Set spending limits for categories and check if you are under or over budget.
9. Monthly Summary Report: Pick a month (like 2026-03) to see your total income, expenses, and savings for that month.
10. Save and Exit: Saves all your data to CSV files so nothing is lost when you close the program.

## Python Concepts Used

Functions: Used to split the code into small, easy parts (like add_transaction() or save_data()).
Lists: Used to store lists of items (like a list of all transactions).
Dictionaries: Used to group details together (like holding a date, category, and amount inside one item).
If/Else Statements: Used to help the computer make decisions (like checking if a menu choice is valid or if you spent too much).
Loops (while and for): Used to keep the menu running and to go through lists item by item.
File Handling: Uses Python's built-in csv tools to read and write files so data is saved to your computer.
Error Handling (try/except): Prevents the program from crashing if someone types a letter instead of a number.

## Data Files

1. budget_data.csv
Saves every transaction you enter.
Date: The date of the transaction (YYYY-MM-DD).
Type: Tells if it is Income or Expense.
Category: What kind of transaction it was (like Food or Salary).
Description: A quick note about what it was for.
Amount: How much money it was.
2. budget_limits.csv
Saves your category spending limits.
Category: The category name (like Food).
Limit: The maximum money you want to spend in that category.

## Testing Summary

Testing Bad Inputs:
Typed letters instead of numbers in the menu. The program showed an error message and did not crash.
Typed negative numbers for amounts. The program asked for a positive number.
Picked numbers that were not on the list. The program told the user the choice was invalid.
Testing File Scenarios:
Started the program without any saved files. The program created brand new files without crashing.

## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.
