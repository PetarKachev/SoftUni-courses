input_info = input()

input_info = input_info.split(" ")

sign = input_info[1]

if sign == "/":
    try:
        first_num = float(input_info[0])
        second_num = float(input_info[2])

        result = first_num / second_num
        print(f'{result:.2f}')
    except(ZeroDivisionError, ValueError):
        print("La devision par zero n'est pas possible et vous pouvez saisir que des nombres decimales")

elif sign == "*":
    try:
        first_num = float(input_info[0])
        second_num = float(input_info[2])

        result = first_num * second_num
        print(f'{result:.2f}')
    except(ValueError):
        print("Vous pouvez saisir que des nombres decimales")

elif sign == "-":
    try:
        first_num = float(input_info[0])
        second_num = float(input_info[2])

        result = first_num - second_num
        print(f'{result:.2f}')
    except(ValueError):
        print("Vous pouvez saisir que des nombres decimales")

elif sign == "+":
    try:
        first_num = float(input_info[0])
        second_num = float(input_info[2])

        result = first_num + second_num
        print(f'{result:.2f}')
    except(ValueError):
        print("Vous pouvez saisir que des nombres decimales")

elif sign == "^":
    try:
        first_num = float(input_info[0])
        second_num = float(input_info[2])

        result = first_num ** second_num
        print(f'{result:.2f}')
    except(ValueError):
        print("Vous pouvez saisir que des nombres decimales")