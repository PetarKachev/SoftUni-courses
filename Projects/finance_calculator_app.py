print('Welcome to the Finance Calculator') # --> TITLE
print('Main Menu:') # --> MENU
print(' 1. Calculate Simple Interest') # --> Simple Interest
print(' 2. Calculate Campound Interest') # --> Campound Interest
print(' 3. Calculate Loan Payment') # --> Loan Payment
print(' 4. Calculate Futur Value of Savings') # -->Futur Value
print(' 5. Quit') # --> Exit
choice = input("Enter your choice (1/2/3/4/5): ") # --> User should choose an option
import sys # --> EXIT
def simple_interest(first, second, third): # This function will calculate the simple interest
    return first * second * third
def compound_interest(P, R, T, N): # This function will calculate the compound interest
    return P * (1 + (R / N)) ** (N * T) - P
def loan_payment(first, second, third): # This function will calculate the loan payment
    return first * (second/third)
def futur_value(first, second, third): # This function will calculate the futur value
    return first * (1 + (second * third))
def main_menu(choice): # This is the main function that we will use
    if choice == "1": # First option --> The formula - Principal amount * Interest rate * Time (In years)
        print('Calculate Simple Interest - User should insert 3 values.') # Title of current calculation
        first_value = input("Enter principal amount (as an integer): ") # User should write a number
        second_value = input("Enter interest rate (as a decimal): ") # User should write a number
        third_value = input("Enter time (in years): ") # User should write a number
        if first_value.isdigit() and second_value.isdigit() and third_value.isdigit() or "." in second_value:
            if not "." in second_value: # If the user wants to write an integer number - % We need to transform it
                second_value = int(second_value) / 100
            if not "." in first_value and not "." in third_value:
                result = simple_interest(int(first_value), float(second_value), int(third_value))
                return f'Simple Interest: ${result:.2f}'
            else:
                return "Invalid operation, try again!"
        else:
            return "Invalid operation, try again!"

    elif choice == "2": # Second option --> The formula - P * (1 + (R / N)) ** (N * T) - P
        print('Calculate Compound Interest - User should insert 4 values.') # Title of current calculation
        first_value = input("Enter principal amount (as an integer): ") # User should write a number
        second_value = input("Enter annual interest rate (as a decimal): ") # User should write a number
        third_value = input("Enter the number of times interest is compounded per year (as an integer): ") # User should write a number
        forth_value = input("Enter time (in years): ") # User should write a number
        if first_value.isdigit() and second_value.isdigit() and third_value.isdigit() and forth_value.isdigit() or "." in second_value:
            if not "." in second_value: # If the user wants to write an integer number - % We need to transform it
                second_value = int(second_value) / 100
            if forth_value != "0" and second_value != "0":
                if "." not in first_value and "." not in third_value and "." not in forth_value:
                    result = compound_interest(int(first_value), float(second_value), int(third_value), int(forth_value))
                    return f'Compound interest: ${result:.2f}'
                else:
                    return f'Invalid operation, try again!'
            else:
                return f'Dividing by zero is impossible!'
        else:
            return "Invalid operation, try again!"

    elif choice == "3": # Third option --> The formula - Principal amount * (Interest rate / 12)
        print('Calculate Loan Payment (Monthly) - User should insert 2 values.') # Title of current calculation
        first_value = input("Enter principal amount (as an integer): ") # User should write a number
        second_value = input("Enter interest rate (as a decimal): ") # User should write a number
        third_value = 12 # This is by default because this is the number of the months in every year
        if first_value.isdigit() and second_value.isdigit() or "." in second_value:
            if not "." in second_value: # If the user wants to write an integer number - % We need to transform it
                second_value = int(second_value) / 100
            if not "." in first_value:
                result = loan_payment(int(first_value), float(second_value), third_value)
                return f'Monthly Loan Payment: ${result:.2f}'
            else:
                return f'Invalid operation, try again!'
        else:
            return 'Invalid operation, try again!'

    elif choice == "4": # Forth option --> The formula - Principal amount * (1 + (Interest rate * Time (In Years)))
        print('Calculate Futur Value of Savings - User should insert 3 values.') # Title of current calculation
        first_value = input("Enter principal amount (as an integer): ") # User should write a number
        second_value = input("Enter interest rate (as a decimal): ") # User should write a number
        third_value = input("Enter time (in years): ") # User should write a number
        if first_value.isdigit() and second_value.isdigit() or "." in second_value:
            if not "." in second_value: # If the user wants to write an integer number - % We need to transform it
                second_value = int(second_value) / 100
            if not "." in first_value and not "." in third_value:
                result = futur_value(int(first_value), float(second_value), int(third_value))
                return f'Futur value: ${result:.2f}'
            else:
                return 'Invalid operation, try again!'
        else:
            return 'Invalid operation, try again!'

    elif choice == "5": # EXIT()
        return "Goodbye!"
        sys.exit()

    else: # EVERYTHING ELSE, WRONG
        return f'Invalid operation, try again!'

print(main_menu(choice)) # --> Main function that we will use

while choice != "5": # --> Only when we have 5, we will leave. Until this moment we will have the options from 1 to 4, everything else will give us error!
    new_choice = input("Do you want to perform another calculation? (yes/no): ")
    if new_choice == "yes": # --> Continue asking the user !
        print('Main Menu:') # --> Main Menu
        print(' 1. Calculate Simple Interest') # --> Simple Interest Calculation
        print(' 2. Calculate Compound Interest') # --> Compound Interest Calculation
        print(' 3. Calculate Loan Payment') # --> Loan Payment Calculation
        print(' 4. Calculate Futur Value of Savings') # --> Futur Value of Savings Calculation
        print(' 5. Quit') # --> EXIT from the program
        choice = input("Enter your choice (1/2/3/4/5): ") # --> User should choose an option from these numbers.
        print(main_menu(choice))
    elif new_choice == "no": # --> Stop, leave.
        print("Goodbye!")
        sys.exit()
    else: # --> ERROR
        print('Invalid operation, try again!')