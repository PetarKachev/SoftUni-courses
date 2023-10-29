num_groups = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(num_groups):
    people = int(input())
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kilimanjaro += people
    elif 26 <= people <= 40:
        k2 += people
    elif people >= 41:
        everest += people

all_people = musala + monblan + kilimanjaro + k2 + everest

musala = musala / all_people * 100
monblan = monblan / all_people * 100
kelimanjaro = kilimanjaro / all_people * 100
k2 = k2 / all_people * 100
everest = everest / all_people * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kelimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")
