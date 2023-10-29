import math

world_record_sec = float(input())
distance_m = float(input())
meters_per_sec = float(input())

time_sec = distance_m * meters_per_sec
delay = math.floor(distance_m / 15) * 12.5

total_time_sec = time_sec + delay
diff = total_time_sec - world_record_sec

if world_record_sec <= total_time_sec:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time_sec:.2f} seconds.")