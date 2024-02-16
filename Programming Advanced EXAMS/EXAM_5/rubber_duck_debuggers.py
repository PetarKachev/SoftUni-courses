from collections import deque
time = deque(list(map(int, input().split(" "))))
number_tasks = deque(list(map(int, input().split(" "))))
dict_with_ducks = {"darth_vader_ducky": 0, "thor_ducky": 0, "big_blue_rubber_ducky": 0, "small_yellow_rubber_ducky": 0}

while time and number_tasks:
    if 0 <= time[0] * number_tasks[-1] <= 60:
        dict_with_ducks["darth_vader_ducky"] += 1
        time.popleft()
        number_tasks.pop()
    elif 61 <= time[0] * number_tasks[-1] <= 120:
        dict_with_ducks["thor_ducky"] += 1
        time.popleft()
        number_tasks.pop()
    elif 121 <= time[0] * number_tasks[-1] <= 180:
        dict_with_ducks["big_blue_rubber_ducky"] += 1
        time.popleft()
        number_tasks.pop()
    elif 181 <= time[0] * number_tasks[-1] <= 240:
        dict_with_ducks["small_yellow_rubber_ducky"] += 1
        time.popleft()
        number_tasks.pop()
    else:
        number_tasks[-1] -= 2
        time.append(time.popleft())

if len(time) == 0 and len(number_tasks) == 0:
    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {dict_with_ducks['darth_vader_ducky']}")
print(f"Thor Ducky: {dict_with_ducks['thor_ducky']}")
print(f"Big Blue Rubber Ducky: {dict_with_ducks['big_blue_rubber_ducky']}")
print(f"Small Yellow Rubber Ducky: {dict_with_ducks['small_yellow_rubber_ducky']}")