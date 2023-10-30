list_with_groceries = input().split("!")

command = input()

while command != "Go Shopping!" and len(list_with_groceries) > 0:
    command = command.split(" ")

    if command[0] == "Urgent":
        item = str(command[1])
        if item not in list_with_groceries:
            list_with_groceries.insert(0, item)

    if command[0] == "Unnecessary":
        item = str(command[1])
        if item in list_with_groceries:
            for i in range(len(list_with_groceries)):
                if i < len(list_with_groceries):
                    if list_with_groceries[i] == item:
                        list_with_groceries.remove(list_with_groceries[i])

    if command[0] == "Correct":
        old_item = str(command[1])
        new_item = str(command[2])
        if old_item in list_with_groceries:
            for i in range(len(list_with_groceries)):
                if list_with_groceries[i] == old_item:
                    list_with_groceries[i] = new_item

    if command[0] == "Rearrange":
        item = str(command[1])
        if item in list_with_groceries:
            for i in range(len(list_with_groceries)):
                if list_with_groceries[i] == item:
                    removed_item = list_with_groceries.pop(i)
                    list_with_groceries.append(removed_item)

    command = input()

print(", ".join(list_with_groceries))