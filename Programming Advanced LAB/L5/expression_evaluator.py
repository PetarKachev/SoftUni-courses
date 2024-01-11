from math import floor
from collections import deque
string = list(map(str, input().split(" ")))
result_deque = deque()

for element in string:

    if element == "*":
        operator_index = string.index("*")
        current_sequence = string[:operator_index]
        string = string[operator_index + 1:]
        for num in current_sequence:
            result_deque.append(int(num))

        result = result_deque.popleft()
        while result_deque:
            result *= result_deque.popleft()

        result_deque.append(result)

    if element == "+":
        operator_index = string.index("+")
        current_sequence = string[:operator_index]
        string = string[operator_index + 1:]
        for num in current_sequence:
            result_deque.append(int(num))

        result = result_deque.popleft()
        while result_deque:
            result += result_deque.popleft()

        result_deque.append(result)

    if element == "-":
        operator_index = string.index("-")
        current_sequence = string[:operator_index]
        string = string[operator_index + 1:]
        for num in current_sequence:
            result_deque.append(int(num))

        result = result_deque.popleft()
        while result_deque:
            result -= result_deque.popleft()

        result_deque.append(result)

    if element == "/":
        operator_index = string.index("/")
        current_sequence = string[:operator_index]
        string = string[operator_index + 1:]
        for num in current_sequence:
            result_deque.append(int(num))

        result = result_deque.popleft()
        while result_deque:
            result /= result_deque.popleft()

        result_deque.append(floor(result))

print(result_deque[0])