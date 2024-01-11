from collections import deque
string = deque(input().split(" "))
main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'orange': ['red', 'yellow'],
                    'purple': ['red', 'blue'],
                    'green': ['yellow', 'blue']}
collected_colors = []

while string:
    first_str = string.popleft()
    last_str = string.pop() if string else ''

    if first_str + last_str in main_colors or first_str + last_str in secondary_colors:
        collected_colors.append(first_str + last_str)
    elif last_str + first_str in main_colors or last_str + first_str in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            string.insert(len(string) // 2, first_str[:-1])
        if len(last_str) > 1:
            string.insert(len(string) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for element in secondary_colors[color]:
            if element not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)