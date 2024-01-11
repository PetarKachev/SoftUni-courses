from collections import deque
first_sequence = set(map(int, input().split(" ")))
second_sequence = set(map(int, input().split(" ")))

n = int(input())

for i in range(n):
    info = input().split(" ")

    if info[0] == "Add" and info[1] == "First":
        numbers_sequence = info[2:]
        numbers_sequence = deque([int(num) for num in numbers_sequence])
        while len(numbers_sequence) > 0:
            first_sequence.add(numbers_sequence.popleft())

    elif info[0] == "Add" and info[1] == "Second":
        numbers_sequence = info[2:]
        numbers_sequence = deque([int(num) for num in numbers_sequence])
        while len(numbers_sequence) > 0:
            second_sequence.add(numbers_sequence.popleft())

    elif info[0] == "Remove" and info[1] == "First":
        numbers_sequence = info[2:]
        numbers_sequence = [int(num) for num in numbers_sequence]
        for num in numbers_sequence:
            if num in first_sequence:
                first_sequence.remove(num)

    elif info[0] == "Remove" and info[1] == "Second":
        numbers_sequence = info[2:]
        numbers_sequence = [int(num) for num in numbers_sequence]
        for num in numbers_sequence:
            if num in second_sequence:
                second_sequence.remove(num)

    elif info[0] == "Check" and info[1] == "Subset":
        if first_sequence >= second_sequence:
            print(True)
        elif second_sequence >= first_sequence:
            print(True)
        else:
            print(False)

first_sequence = sorted([int(element) for element in first_sequence])
second_sequence = sorted([int(element) for element in second_sequence])
print(', '.join([str(element) for element in first_sequence]))
print(', '.join([str(element) for element in second_sequence]))