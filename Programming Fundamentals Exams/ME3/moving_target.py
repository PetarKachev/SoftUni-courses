sequence_of_integers = list(map(int, input().split()))
command = input()

while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        shoot_index = int(command[1])
        shoot_power = int(command[2])
        if 0 <= shoot_index < len(sequence_of_integers):
            sequence_of_integers[shoot_index] -= shoot_power
            if sequence_of_integers[shoot_index] <= 0:
                sequence_of_integers.remove(sequence_of_integers[shoot_index])
    elif command[0] == "Add":
        add_index = int(command[1])
        add_value = int(command[2])
        if 0 <= add_index < len(sequence_of_integers):
            sequence_of_integers.insert(add_index, add_value)
        else:
            print('Invalid placement!')
    elif command[0] == "Strike":
        strike_index = int(command[1])
        strike_radius = int(command[2])
        start = strike_index - strike_radius
        end = strike_index + strike_radius
        if start >= 0 and end < len(sequence_of_integers):
            del sequence_of_integers[start: end + 1]
        else:
            print("Strike missed!")
    command = input()
result = ""
for word in range(len(sequence_of_integers) - 1):
    result += str(sequence_of_integers[word]) + "|"

print(result + str(sequence_of_integers[-1]))
