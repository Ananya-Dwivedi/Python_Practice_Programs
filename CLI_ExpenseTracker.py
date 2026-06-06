
from datetime import date

def add_expense(expenses, amount, category, description):
    if amount<=0 :
        raise ValueError(f"Amount must be greater than zero .")
    if  category not in ["food","transport","shopping","bills","other"]: 
        raise ValueError(f"{amount} is not a valid category .")
    expense={
            "amount":amount,
            "category":category,
            "description":description,
            "date": date.today()
        }
    expenses.append(expense)
    print(f"Expense added successfully.")
    
   
   

def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print(f"Expenses : \n")
    total= 0
    for expense in expenses:
        print(f"{expense["amount"]} |  {expense["category"]}  |  {expense["description"]}  |  {expense["date"]}")
        total += expense['amount']
    print(f"\nTotal spent: Rs {total}")
   

def total_by_category(expenses):
    totals={}
    for expense in expenses:
        category = expense["category"]
        if category not in totals:
            totals[category] = 0
        total[category] += expense["amount"]
    
    print("\nTotal by category:")
    for category, total in totals.items():
        print(f"{category}: Rs {total}")
#    food_exp=transport_exp=shopping_exp=bills_exp=other_exp=0
#    for expense in expenses:
#        if expense["category"]=="food":
#            food_exp+=expense["amount"]
#        elif expense["category"]=="transport":
#            transport_exp+=expense["amount"]
#        elif expense["category"]=="shopping":
#            shopping_exp+=expense["amount"]     
#        elif expense["category"]=="bills":
#            bills_exp+=expense["amount"]
#        elif expense["category"]=="other":
#            other_exp+=expense["amount"]
        

def save_expenses(expenses):
    
    with open("expenses.txt", "w") as f:
        for expense in expenses:
            f.write(f"{expense['amount']}|{expense['category']}|{expense['description']}|{expense['date']}\n")
    print("Expenses saved successfully.")
       

def load_expenses():
    # with open("expenses.txt","r") as f :
    #    content=f.readlines()
    #    return content
  
    expenses = []
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split("|")
                expense = {
                    "amount": float(parts[0]),
                    "category": parts[1],
                    "description": parts[2],
                    "date": parts[3]
                }
                expenses.append(expense)
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.")
    return expenses
   

def main():
   
    expenses = load_expenses()  # load existing data on startup
    print(expenses)
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total by category")
        print("4. Save expenses")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            try:
                add_expense(expenses, amount, category, description)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_by_category(expenses)
        elif choice == "4":
            save_expenses(expenses)
        elif choice == "5":
            save_expenses(expenses)
            load_expenses()
            print("Bye!")
            break

main()