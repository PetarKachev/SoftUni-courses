number_of_commands = int(input())

dictionary_with_users = {}

for command in range(number_of_commands):
    current_command = input().split(" ")

    if current_command[0] == "register":
        username = str(current_command[1])
        license = str(current_command[2])

        if username in dictionary_with_users.keys():
            print(f"ERROR: already registered with plate number {license}")
            continue
        dictionary_with_users[username] = license
        print(f"{username} registered {license} successfully")

    elif current_command[0] == "unregister":
        username = str(current_command[1])

        if username not in dictionary_with_users.keys():
            print(f"ERROR: user {username} not found")
            continue
        del dictionary_with_users[username]
        print(f"{username} unregistered successfully")

for key, value in dictionary_with_users.items():
    print(f'{key} => {value}')