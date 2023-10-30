x = float(input())
y = float(input())
h = float(input())

front_and_back_walls = 2 * (x * x) - (1.2 * 2)
rear_walls = 2 * (x * y) - 2 * (1.5 * 1.5)
front_roof = 2 * (x * h / 2)
rear_roof = 2 * (x * y)

all_walls = (front_and_back_walls + rear_walls)
all_roof = (front_roof + rear_roof)

walls_lt = all_walls / 3.4
roof_lt = all_roof / 4.3

print(f"{walls_lt:.2f}")
print(f"{roof_lt:.2f}")