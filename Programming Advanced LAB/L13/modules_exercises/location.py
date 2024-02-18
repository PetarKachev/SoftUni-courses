def locate(sequence, number: int):
    result = ''

    sequence = [int(el) for el in sequence]

    if number in sequence:
        needed_index = sequence.index(number)
        result += f'The number - {number} is at index {needed_index}'

    else:
        result += f'The number {number} is not in the sequence'

    return result