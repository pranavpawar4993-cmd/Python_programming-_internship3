

import json
import os
from datetime import datetime

DB_FILE = "expenses.json"

def get_saved_expenses():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return [] # fallback strategy for bad files

def commit_to_file(data):
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=3)
    except Exception as e:
        print(f"Error updating database file: {e}")

def enter_new_expense(all_expenses):
    print("\n--- Track New Expense ---")
    try:
        amt = float(input("Amount spent: $"))
        cat = input("Category (e.g. Food, Travel, Bills): ").strip().title()
        desc = input("Brief Description: ").strip()
    except ValueError:
        print("Error: Invalid numeric input for amount entry.")
        return

    # Auto generate localized date stamp strings
    now_stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    new_row = {
        "date": now_stamp,
        "category": cat,
        "amount": amt,
        "description": desc
    }
    
    all_expenses.append(new_row)
    commit_to_file(all_expenses)
    print("Expense tracked successfully.")

def run_analytics_menu(all_expenses):
    if not all_expenses:
        print("No transactions recorded to build reports.")
        return
        
    while True:
        print("\n--- Analytics & Reporting Menu ---")
        print("1. Display all recorded logs")
        print("2. Display breakdowns by category")
        print("3. Back to main screen")
        
        sub_choice = input("Enter choice: ").strip()
        
        if sub_choice == '1':
            print(f"\n{'Date & Time':<17} | {'Category':<12} | {'Amount':<8} | {'Description'}")
            print("-" * 65)
            grand_total = 0
            for exp in all_expenses:
                print(f"{exp['date']:<17} | {exp['category']:<12} | ${exp['amount']:<7.2f} | {exp['description']}")
                grand_total += exp['amount']
            print("-" * 65)
            print(f"Net Total Outflow: ${grand_total:.2f}\n")
            
        elif sub_choice == '2':
            # Accumulate category group buckets manually
            breakdown = {}
            for exp in all_expenses:
                c = exp['category']
                breakdown[c] = breakdown.get(c, 0.0) + exp['amount']
                
            print(f"\n{'Category':<15} | {'Total Cost'}")
            print("-" * 30)
            for cat, total in breakdown.items():
                print(f"{cat:<15} | ${total:.2f}")
            print("-" * 30 + "\n")
            
        elif sub_choice == '3':
            break
        else:
            print("Invalid menu selection.")

def main():
    expense_list = get_saved_expenses()
    
    while True:
        print("=== Expense Monitor tool ===")
        print("1. Log New Expense")
        print("2. Reports and Summaries")
        print("3. Exit Tracker")
        
        usr_choice = input("Select an option: ").strip()
        if usr_choice == '1':
            enter_new_expense(expense_list)
        elif usr_choice == '2':
            run_analytics_menu(expense_list)
        elif usr_choice == '3':
            print("Closing application manager. Check your local JSON database for updates.")
            break
        else:
            print("Invalid choice options. Pick again.\n")

if __name__ == "__main__":
    main()
