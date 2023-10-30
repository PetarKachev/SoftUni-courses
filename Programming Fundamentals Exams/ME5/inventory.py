items_list = input().split(", ")

command = input()

while command != "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        item = str(command[1])
        if not item in items_list:
            items_list.append(item)
    elif command[0] == "Drop":
        item = command[1]
        if item in items_list:
            items_list.remove(item)
    elif command[0] == "Combine Items":
        new_command = command[1].split(":")
        old_item = new_command[0]
        new_item = new_command[1]
        for i in range(len(items_list)):
            if items_list[i] == old_item:
                items_list.insert(i + 1, new_item)
    elif command[0] == "Renew":
        item = command[1]
        for i in range(len(items_list)):
            if items_list[i] == item:
                items_list.remove(items_list[i])
                items_list.append(item)
    command = input()
result =""
for i in range(len(items_list) - 1):
    result += f'{items_list[i]}, '

print(result + items_list[-1])