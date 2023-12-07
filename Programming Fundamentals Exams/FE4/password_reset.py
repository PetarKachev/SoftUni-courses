string = input()
command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        new_string = ''
        for character in range(len(string)):
            if character % 2 != 0:
                new_string += string[character]
        string = new_string
        print(string)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        string = string[:index] + string[index + length:]
        print(string)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {string}")