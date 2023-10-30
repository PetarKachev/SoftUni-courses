number = int(input())

for i in range(1, number + 1):
    code_message = int(input())

    if code_message == 88:
        print('Hello')
    elif code_message == 86:
        print('How are you?')
    elif code_message != 88 and code_message != 86 and code_message < 88:
        print('GREAT!')
    elif code_message > 88:
        print("Bye.")