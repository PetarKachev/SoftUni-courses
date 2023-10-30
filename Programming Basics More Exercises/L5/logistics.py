number_of_loads = int(input())

minivan_load_tons = 0
truck_load_tons = 0
train_load_tons = 0

total_tons = 0
total_income = 0

for _ in range(1, number_of_loads + 1):
    current_load = int(input())
    total_tons += current_load
    if current_load <= 3:   # minivan
        current_income = current_load * 200
        total_income += current_income
        minivan_load_tons += current_load

    elif 4 <= current_load <= 11:   # truck
        current_income = current_load * 175
        total_income += current_income
        truck_load_tons += current_load
    elif current_load >= 12:    # train
        current_income = current_load * 120
        total_income += current_income
        train_load_tons += current_load

avg_total_income = total_income / total_tons
minivan_percent = minivan_load_tons / total_tons * 100
truck_percent = truck_load_tons / total_tons * 100
train_percent = train_load_tons / total_tons * 100

print(f"{avg_total_income:.2f}")
print(f"{minivan_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
