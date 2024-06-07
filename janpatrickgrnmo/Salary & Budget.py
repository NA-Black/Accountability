import time
import os
import platform

def system_id_clear():
    from sys import platform

    if platform == "linux" or platform == "linux2":
        return "clear"
    elif platform == "darwin":
        return "clear"
    elif platform == "win32":
        return "cls"


def calculate_salary_and_budget():
    print("Welcome! This program will automatically calculate your Salary & Budget for every cut-off.")
    time.sleep(2)
    while True:
        try:
            num_salaries = int(input("\nHow many salaries would you like to input? "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid integer for the number of salaries.")
    
    salaries = []
    for i in range(num_salaries):
        while True:
            try:
                salary = float(input(f"\nEnter Net Salary #{i+1}: PHP "))
                salaries.append(salary)
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid float for the net salary.")
    
    while True:
        try:
            emergency_fund_percentage = float(input("\nEnter the percentage of salary to allocate to the Emergency Fund: "))
            if 0 <= emergency_fund_percentage <= 100:
                break
            else:
                print("\nInvalid input. Please enter a percentage between 0 and 100.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number for the percentage.")
    
    # Calculate the total emergency fund based on user-defined percentage
    total_emergency_fund = sum(salary * (emergency_fund_percentage / 100) for salary in salaries)
    
    while True:
        create_budget = input("\nWould you like to create a budget allocation for your Spending Money? (yes/no): ").strip().lower()
        if create_budget in ['yes', 'no']:
            
            #for clearing the terminal
            os_id_clear = system_id_clear()
            os.system(os_id_clear)
            break
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")
    
    if create_budget == 'yes':
        while True:
            budget_items = {}
            total_percentage = 0
            while total_percentage != 100:
                print("\nPlease enter your budget allocation items and their percentage (Type 'Reset' to Clear Budget Allocation): ")
                budget_items.clear()
                total_percentage = 0
                reset_flag = False
                while total_percentage < 100:
                    item = input("\nBudget Item: ").strip().lower()
                    if item == 'reset':
                        print("\nYour budget allocation inputs have been reset.")
                        print("\n" + "\n" * 50)
                        reset_flag = True
                        break
                    if item in budget_items:
                        print(f"\nThe item '{item}' has already been entered. Please enter a different item.")
                        continue
                    while True:
                        try:
                            percentage = float(input(f"Percentage for {item}: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please enter a valid number for the percentage.\n")
                    if total_percentage + percentage > 100:
                        print(f"\nAdding {percentage}% for {item} exceeds the total of 100%. Please re-enter this item.")
                        continue
                    budget_items[item] = percentage
                    total_percentage += percentage
                    remaining_percentage = 100 - total_percentage
                    print(f"\nRemaining percentage: {remaining_percentage}%")
                if reset_flag:
                    break
                if total_percentage == 100:
                    break
                else:
                    print("\nThe total percentage for all budget items must be equal to 100%. Try again.")
            if total_percentage == 100:
                break
        
        total_spending_money = sum(salary * (1 - emergency_fund_percentage / 100) for salary in salaries)
        budget_allocation = {}
        for item, percentage in budget_items.items():
            budget_allocation[item] = sum(salary * (1 - emergency_fund_percentage / 100) * (percentage / 100) for salary in salaries)
        
        # Page break before presenting the salary and budget
        print("\n" + "\n" * 50)
        print("Computing Salary & Budget...")
        time.sleep(2)
        print(f"\nSALARY:\n")
        print(f"Total Spending Money: PHP {total_spending_money:.2f}")
        print(f"Total Emergency Fund: PHP {total_emergency_fund:.2f}")
        print("\nBUDGET:\n")
        for item, amount in budget_allocation.items():
            print(f"Total {item.capitalize()}: PHP {amount:.2f}")
    else:
        # Page break before presenting the salary
        print("\n" + "\n" * 50)
        print("\nBudget allocation skipped.\n")
        total_spending_money = sum(salary * (1 - emergency_fund_percentage / 100) for salary in salaries)
        print("Computing your Spending Money & Emergency Fund...\n")
        time.sleep(2)
        print("SALARY:")
        print(f"\nTotal Spending Money: PHP {total_spending_money:.2f}")
        print(f"Total Emergency Fund: PHP {total_emergency_fund:.2f}")
    
    print("\nThank you! Always remember to spend your money wisely.\n")

if __name__ == "__main__":
    calculate_salary_and_budget()
