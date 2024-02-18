from creation import create
from location import locate

command = input()
current_sequence = ''

while command != "Stop":
    command = command.split(" ")

    if command[0] == "Create":
        number = int(command[2])
        current_sequence = create(number)
        result = create(number)
        result = ' '.join(str(el) for el in result)
        print(result)

    elif command[0] == "Locate":
        number = int(command[1])
        print(locate(current_sequence, number))
        current_sequence = ''

    command = input()