import os
command = input()

while command != "End":
    command = command.split("-")
    if command[0] == "Create":
        file_name = command[1]
        with open(file_name, "w") as f:
            f.write('')

    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(file_name, "a") as f:
            f.write(f'{content}\n')

    elif command[0] == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(file_name):
            file_name.replace(old_string, new_string)
        else:
            print("An error occurred")

    elif command[0] == "delete":
        file_name = command[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input()