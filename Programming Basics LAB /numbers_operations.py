num1 = int(input())
num2 = int(input())
operator = input()
result = 0
zero_flag = False

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        zero_flag = True
    else:
        result = num1 / num2
elif operator == '%':
    if num2 == 0:
        zero_flag = True
    else:
        result = num1 % num2

if operator == '+' or operator == '-' or operator == '*':
    if result % 2 == 0:
        print(f"{num1} {operator} {num2} = {result} - even")
    else:
        print(f"{num1} {operator} {num2} = {result} - odd")
elif operator == '/':
    if zero_flag:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} / {num2} = {result:.2f}")
elif operator == '%':
    if zero_flag:
        print(f"Cannot divide {num1} by zero")
    else:
        print(f"{num1} % {num2} = {result}")
