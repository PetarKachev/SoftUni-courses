rest_days = int(input())

rest_days_play = rest_days * 127
work_days_play = (365 -rest_days) * 63
all_play_min = rest_days_play + work_days_play

diff_min = abs(30000 - all_play_min)

if 30000 >= all_play_min:
   diff = 30000 - all_play_min
   hours = diff // 60
   minutes = diff % 60
   print(f"Tom sleeps well")
   print(f"{hours} hours and {minutes} minutes less for play")
else:
    hours = diff_min // 60
    minutes = diff_min % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
