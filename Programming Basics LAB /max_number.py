from sys import maxsize

max_number = -maxsize

while True:
    data = input()
    if data == 'Stop':
        break

    current_number = int(data)

    if current_number > max_number:
        max_number = current_number

print(max_number)
