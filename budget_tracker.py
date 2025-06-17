import json

def add_expense(expenses,descriptions, amount):
    expenses.append({"descriptions" : descriptions, "amount" : amount})
    print(f"Added expense : {descriptions} , {amount}")


def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


def show_budget_details(budget, expenses):
    print(f"Total budget is {budget}")
    print("Expenses: ")
    for expense in expenses:
        print(f" -{expense['descriptions']} : {expense['amount']}")
    print(f"Total Spend : {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.loads(file)
            return data["initial_budget"], data["budget"]
    except(FileNotFoundError, json.JSONDecodeError):
        return 0, []
    
def save_budget_details(filepath,initial_budget,expenses):
    data = {
        "initial_budget" : initial_budget,
        "expenses": expenses
    }
    with open(filepath,"w") as file:
        json.dump(data,file,indent=4)


def main():
    print("Welcome to the Budget App")
    initial_budget = float(input("Please enter your initial budget : "))
    filepath = "budget_data.json"
    if initial_budget == 0 :
        initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do ?")
        print("1. Add an expense")
        print("2. Show Budget Detail")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            descriptions = input("Enter expense description: ")
            amount = float(input("Enter expense amount"))
            add_expense(expenses,descriptions, amount)
        if choice == "2":
            show_budget_details(budget, expenses)
        if choice == "3":
            save_budget_details(filepath,initial_budget,expenses)
            print("Exiting from App, Goodbye!!!")
            break
        else:
            print("Your choice is Invalid")

if __name__ == "__main__":
    main()
