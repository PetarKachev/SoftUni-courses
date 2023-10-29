init_hours = int(input())
init_minutes = int(input())

total_time_min = (init_hours * 60) + init_minutes + 15

hours = total_time_min // 60
minutes = total_time_min % 60

if 0 <= hours <= 23:
    print(f"{hours}:{minutes:02}")
elif hours == 24:
    hours = 0
    print(f"{hours}:{minutes:02}")
elif hours > 24:
    print("Error")