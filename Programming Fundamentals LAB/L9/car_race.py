time_per_car = list(map(int, input().split(" ")))

first_car = time_per_car[0]
final_car = time_per_car[-1]
middle_index = len(time_per_car) // 2

time_first_racer = 0
time_second_racer = 0

for current_time1 in range(len(time_per_car)):
    if current_time1 < middle_index:
        time_first_racer += int(time_per_car[current_time1])
        if time_per_car[current_time1] == 0:
            time_first_racer -= (time_first_racer * 0.20)

for current_time2 in range(len(time_per_car) -1, -1, -1):
    if current_time2 > middle_index:
        time_second_racer += int(time_per_car[current_time2])
        if time_per_car[current_time2] == 0:
            time_second_racer -= (time_second_racer * 0.20)

if time_first_racer < time_second_racer:
    print(f'The winner is left with total time: {time_first_racer:.1f}')
else:
    print(f'The winner is right with total time: {time_second_racer:.1f}')