junior_cyclists = int(input())
senior_cyclists = int(input())
race_track_type = input()

race_tax = 0

if race_track_type == "trail":
    race_tax += junior_cyclists * 5.50
    race_tax += senior_cyclists * 7
elif race_track_type == "cross-country":
    race_tax += junior_cyclists * 8
    race_tax += senior_cyclists * 9.50
elif race_track_type == "downhill":
    race_tax += junior_cyclists * 12.25
    race_tax += senior_cyclists * 13.75
elif race_track_type == "road":
    race_tax += junior_cyclists * 20
    race_tax += senior_cyclists * 21.50

if race_track_type == "cross-country" and junior_cyclists + senior_cyclists >= 50:
    race_tax *= 0.75

race_tax *= 0.95

print(f"{race_tax:.2f}")
