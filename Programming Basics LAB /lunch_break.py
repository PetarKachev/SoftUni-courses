import math

name_series = str(input())
ep_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

time_left = break_duration - lunch_time - relax_time

diff = abs(time_left - ep_duration)
rounded_diff = math.ceil(diff)

if time_left >= ep_duration:
    print(f"You have enough time to watch {name_series} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {rounded_diff} more minutes.")