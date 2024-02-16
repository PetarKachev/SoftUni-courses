from collections import deque
working_bees = deque(list(map(int, input().split(" "))))
nectar = deque(list(map(int, input().split(" "))))
symbols_honey_process = deque(list(map(str, input().split(" "))))
collected_honey = deque([])

while len(working_bees) > 0 and len(nectar) > 0:
    if len(working_bees) == 0 or len(nectar) == 0:
        break

    if working_bees[0] <= nectar[-1]:
        current_bee = working_bees[0]
        current_collected_honey = nectar[-1]
        current_operator = symbols_honey_process[0]

        if current_operator == "/" and current_collected_honey == 20:
            working_bees.popleft()
            nectar.pop()
            symbols_honey_process.popleft()
            break

        if current_operator == "+":
            current_result = current_bee + current_collected_honey
            collected_honey.append(abs(current_result))
            working_bees.popleft()
            nectar.pop()
            symbols_honey_process.popleft()

        elif current_operator == "-":
            current_result = current_bee - current_collected_honey
            collected_honey.append(abs(current_result))
            working_bees.popleft()
            nectar.pop()
            symbols_honey_process.popleft()

        elif current_operator == "*":
            current_result = current_bee * current_collected_honey
            collected_honey.append(abs(current_result))
            working_bees.popleft()
            nectar.pop()
            symbols_honey_process.popleft()

        elif current_operator == "/":
            current_result = current_bee / current_collected_honey
            collected_honey.append(abs(current_result))
            working_bees.popleft()
            nectar.pop()
            symbols_honey_process.popleft()

    else:
        nectar.pop()

print(f"Total honey made: {sum(collected_honey)}")
if len(working_bees) > 0:
    print(f"Bees left: {', '.join([str(element) for element in working_bees])}")
if len(nectar) > 0:
    print(f"Nectar left: {', '.join([str(element) for element in nectar])}")