notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    priority = int(command[0]) - 1
    note = command[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [number for number in notes if number != 0]
print(result)
