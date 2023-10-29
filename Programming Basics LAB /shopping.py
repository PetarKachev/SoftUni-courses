budget = float(input())
video_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_sum = video_count * 250
cpu_sum = cpu_count * (video_sum * 0.35)
ram_sum = ram_count * (video_sum * 0.10)

total_sum = video_sum + cpu_sum + ram_sum

if video_count > cpu_count:
    total_sum = total_sum * 0.85
diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")