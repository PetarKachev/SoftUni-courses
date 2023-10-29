import math

tournaments = int(input())
starting_points = int(input())
total_points = starting_points
tournaments_won = 0

for _ in range(tournaments):
    achievement = input()
    if achievement == 'W':
        total_points += 2000
        tournaments_won += 1
    elif achievement == 'F':
        total_points += 1200
    elif achievement == 'SF':
        total_points += 720

average_points = (total_points - starting_points) / tournaments
tournaments_won_percent = (tournaments_won / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)} ")
print(f"{tournaments_won_percent:.2f}%")
