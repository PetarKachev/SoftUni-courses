from string import punctuation
file = open("text.txt", "r")
counter_row = 0

for element in file:
    counter_row += 1
    current_letters = 0
    current_other_symbols = 0
    for nested_element in element:
        if str(nested_element).isalpha():
            current_letters += 1
        elif nested_element in punctuation:
            current_other_symbols += 1
    result = f'Line {counter_row}: {element} ({current_letters})({current_other_symbols})'
    with open("output.txt", "a") as f:
        f.write(f'{result}\n')