from collections import deque
seats = list(map(str, input().split(", ")))
first_sequence = deque(list(map(int, input().split(", "))))
second_sequence = deque(list(map(int, input().split(", "))))
seated_people = []
rotations = 0

while len(seated_people) < 3 and rotations < 10:
    ascii_char = chr(first_sequence[0] + second_sequence[-1])
    first_char = str(first_sequence[0]) + ascii_char
    second_char = str(second_sequence[-1]) + ascii_char

    if first_char in seats:
        if first_char not in seated_people:
            seated_people.append(first_char)
        first_sequence.popleft()
        second_sequence.pop()
        rotations += 1

    elif second_char in seats:
        if second_char not in seated_people:
            seated_people.append(second_char)
        first_sequence.popleft()
        second_sequence.pop()
        rotations += 1

    else:
        first_sequence.insert(len(first_sequence), first_sequence.popleft())
        second_sequence.insert(0, second_sequence.pop())
        rotations += 1

print(f"Seat matches: {', '.join(seated_people)}")
print(f'Rotations count: {rotations}')