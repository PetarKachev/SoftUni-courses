print("Python Calculator") # --- TITLE
print("Menu:") # --- MENU
print(" 1. Addition") # --- +
print(" 2. Subtraction") # --- -
print(" 3. Multiplication") # --- *
print(" 4. Division") # --- /
print(" 5. Quit") # --- EXIT
number = input("Enter your choice (1/2/3/4/5): ") # USER SHOULD CHOOSE AN OPTION
import sys
def addition(first, second): # FUNC FOR ADDITION
    return f'Result: {first} + {second} = {first + second}'
def subtraction(first, second): # FUNC FOR SUBTRACTION
    return f'Result: {first} - {second} = {first - second}'
def multiplication(first, second): # FUNC FOR MULTIPLICATION
    return f'Result: {first} * {second} = {first * second}'
def division(first, second): # FUNC FOR DIVISION
    return f'Result: {first} / {second} = {int(first / second)}'
def main(number): # Enter your choice (1/2/3/4/5)
    if number == "1": # FIRST_OPTION +
        first_num = input("Enter the first number: ")
        second_num = input("Enter the second number: ")
        if first_num.isdigit() and second_num.isdigit():
            result = addition(int(first_num), int(second_num))
            return result
        else:
            return "Invalid number! Try again."

    elif number == "2": # SECOND_OPTION -
        first_num = input("Enter the first number: ")
        second_num = input("Enter the second number: ")
        if first_num.isdigit() and second_num.isdigit():
            result = subtraction(int(first_num), int(second_num))
            return result
        else:
            return "Invalid number! Try again."

    elif number == "3": # THIRD_OPTION *
        first_num = input("Enter the first number: ")
        second_num = input("Enter the second number: ")
        if first_num.isdigit() and second_num.isdigit():
            result = multiplication(int(first_num), int(second_num))
            return result
        else:
            return "Invalid number! Try again."

    elif number == "4": # FORTH_OPTION /
        first_num = input("Enter the first number: ")
        second_num = input("Enter the second number: ")
        if first_num.isdigit() and second_num.isdigit():
            result = division(int(first_num), int(second_num))
            return result
        else:
            return "Invalid number! Try again."

    elif number == "5": # FIFTH OPTION EXIT()
        print("Goodbye!")
        sys.exit()
    else: # EVERYTHING ELSE, WRONG!
        return "Wrong command, try again!"
while True: # THE PROGRAM WILL STOP WHEN WE HAVE - 5
    print(main(number))
    number = input("Enter your choice (1/2/3/4/5): ")