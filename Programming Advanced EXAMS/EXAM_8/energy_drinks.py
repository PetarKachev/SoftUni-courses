from collections import deque
caffeine = deque(list(map(int, input().split(", "))))
energy_drinks = deque(list(map(int, input().split(", "))))
max_caffeine = 300
current_caffeine = 0

while caffeine and energy_drinks:

    if caffeine[-1] * energy_drinks[0] + current_caffeine <= max_caffeine:
        current_caffeine += caffeine[-1] * energy_drinks[0]
        caffeine.pop()
        energy_drinks.popleft()
    else:
        caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0

if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join([str(el) for el in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")