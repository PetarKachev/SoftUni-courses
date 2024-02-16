from collections import deque
food = deque(list(map(int, input().split(', '))))
stamina = deque(list(map(int, input().split(', '))))
conquered_peaks = []
list_peaks = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])
list_values = deque([80, 90, 100, 60, 70])
days = 0

while food and stamina and days < 7:
    if len(list_peaks) == 0:
        break
    if food[-1] + stamina[0] >= list_values[0]:
        conquered_peaks.append(list_peaks.popleft())
        list_values.popleft()
        food.pop()
        stamina.popleft()
        days += 1
    else:
        food.pop()
        stamina.popleft()
        days += 1

if len(list_peaks) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if len(conquered_peaks) > 0:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)