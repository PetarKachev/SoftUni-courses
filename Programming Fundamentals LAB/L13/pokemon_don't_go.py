sequence_of_numbers = list(map(int, input().split(" ")))

all_removed_elements = 0

while len(sequence_of_numbers) > 0:
    integer = int(input())

    if integer < 0:
        current_removed_element = sequence_of_numbers[0]
        all_removed_elements += current_removed_element
        sequence_of_numbers[0], sequence_of_numbers[-1] = sequence_of_numbers[-1], sequence_of_numbers[-1]
        for i in range(len(sequence_of_numbers)):
            if sequence_of_numbers[i] <= current_removed_element:
                sequence_of_numbers[i] += current_removed_element

            elif sequence_of_numbers[i] > current_removed_element:
                sequence_of_numbers[i] -= current_removed_element

    elif integer > len(sequence_of_numbers) -1:
        current_removed_element = sequence_of_numbers[-1]
        all_removed_elements += current_removed_element
        sequence_of_numbers[0], sequence_of_numbers[-1] = sequence_of_numbers[0], sequence_of_numbers[0]
        for i in range(len(sequence_of_numbers)):
            if sequence_of_numbers[i] <= current_removed_element:
                sequence_of_numbers[i] += current_removed_element

            elif sequence_of_numbers[i] > current_removed_element:
                sequence_of_numbers[i] -= current_removed_element

    else:
        removed_element = sequence_of_numbers.pop(integer)
        all_removed_elements += removed_element

        for i in range(len(sequence_of_numbers)):
            if sequence_of_numbers[i] <= removed_element:
                sequence_of_numbers[i] += removed_element

            elif sequence_of_numbers[i] > removed_element:
                sequence_of_numbers[i] -= removed_element

print(all_removed_elements)

