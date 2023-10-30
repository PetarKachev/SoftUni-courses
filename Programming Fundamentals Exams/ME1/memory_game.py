sequence_of_digits = input().split()
moves = 0
command = input()
while command != "end":
    moves += 1
    first_index = int(command.split()[0])
    second_index = int(command.split()[1])
    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(sequence_of_digits) or second_index >= len(sequence_of_digits):
        sequence_of_digits.insert(int(len(sequence_of_digits) / 2), f'-{moves}a')
        sequence_of_digits.insert(int(len(sequence_of_digits) / 2), f'-{moves}a')
        print(f"Invalid input! Adding additional elements to the board")
    elif sequence_of_digits[first_index] == sequence_of_digits[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_digits[first_index]}!")
        variable = sequence_of_digits.pop(first_index)
        sequence_of_digits.remove(variable)
    elif sequence_of_digits[first_index] != sequence_of_digits[second_index]:
        print(f'Try again!')
    if len(sequence_of_digits) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()

if command == "end":
    print('Sorry you lose :(')
    for i in sequence_of_digits:
        print(i, end=" ")