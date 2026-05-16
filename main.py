# improving Project calculator (last day of this project, fixing small issues) and day 12 of learnig python#
def get_number():
    while True:
        num = input("Enter a number: ")
        try:
            num = float(num)
            return num
        except:
            print ("Invalid input! Please enter a number.")

def get_operation():
    return (input("Enter the operation (+, -, *, /): "))

def addition(num1, num2):
    return num1 + num2
def substraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1*num2
def division(num1, num2):
    if num2 == 0:
        return "Division_error"
    elif num2 != 0:
        return num1/num2

def calculate (num1, num2, operation):
    calculator={
        "+" : addition,
        "-" : substraction,
        "*" : multiplication,
        "/" : division
    }
    operation_func = calculator.get(operation)
    if not operation_func:
        return "invalid_operator"
    else:
        return operation_func(num1, num2)

def history(result_history):
    if not result_history:
        print("No history yet")
    else:
        for history_count, history_show in enumerate (result_history, start=1):
            print(f"{history_count}) {history_show}")

def confirmation_func():
    while True:
        confirmation_cal = input("\nDo you want to do this calculation?\n")
        if confirmation_cal.lower() in ["yes","y"]:
            return True
        elif confirmation_cal.lower() in ["no","n"]:
            return False
        else:
            print(f"\nInvalid input! Please enter yes or no.")

def redo_func(redo_store):
    num1 = redo_store.get("first number")
    num2 = redo_store.get("second number")
    operation = redo_store.get("operator")
    if (num1 == None) and (num2 == None) and (operation == None):
        return None
    else:
        return calculate(num1, num2, operation)

def main():
    print("Write the calculation you wanted to do, after each info press enter:")
    result_history = []
    redo_store = None
    while True:
        continue_choice = input("\n------MENU------\n1. Calculate\n2. History\n3. Exit\n4. Clear History\n5. Redo\n\nEnter your choice (1-5): ")
        if continue_choice.lower() in ["exit","3"]:
            print("Thanks for using!")
            break
        elif continue_choice.lower() in ["history","2"]:
            print(f"\n------HISTORY-------\n")
            history(result_history)
        elif continue_choice.lower() in ["calculate", "1"]:
            print()
            while True:
                num1 = get_number()
                operation = get_operation()
                num2 = get_number()
                confirmation = confirmation_func()
                if confirmation:

                    break
                else:
                    print(f"\nCalculation cancelled, try again.\n")
            calculation_outcome = calculate(num1, num2, operation)
            if calculation_outcome == "invalid_operator":
                print(f"\nInvalid operator. Please choose +,-,*,or /")
                continue
            elif calculation_outcome == "Division_error":
                print(f"\nCannot divide by 0!")
                continue
            result = str(num1) + " " + operation + " " + str(num2) + " = " + str(calculation_outcome)
            result_history.append(result)
            redo_store={
                "first number" : num1,
                "second number" : num2,
                "operator" : operation 
            }
            print(f"\nYour result is: {calculation_outcome}")
            print(f"\nReturning to menu.")
        elif continue_choice.lower() in ["clear","4","clear history"]:
            result_history.clear()
            print(f"\nHistory cleared!")
        elif continue_choice.lower() in ["redo","5"]:
            if redo_store:
                print(f"\n{redo_store.get("first number")} {(redo_store.get("operator"))} {(redo_store.get("second number"))} = {(redo_func(redo_store))}") 
            elif not redo_store:
                print(f"\nNo previous calculation to redo!")
        else:
            print(f"\nInvalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()