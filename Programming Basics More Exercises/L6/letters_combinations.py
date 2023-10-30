starting_letter = input()
ending_letter = input()
invalid_letter = input()
combination = ""
combinations_counter = 0

for first in range(ord(starting_letter), ord(ending_letter) + 1):
    for second in range(ord(starting_letter), ord(ending_letter) + 1):
        for third in range(ord(starting_letter), ord(ending_letter) + 1):
            combination = chr(first) + chr(second) + chr(third)
            if invalid_letter in combination:
                continue
            combinations_counter += 1
            print(combination, end=" ")
print(combinations_counter)
