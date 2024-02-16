from collections import deque
textiles = deque(list(map(int, input().split(" "))))
medicaments = deque(list(map(int, input().split(" "))))

created_elements = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:

    first = textiles[0]
    second = medicaments[-1]

    if first + second == 30:
        created_elements["Patch"] += 1
        textiles.popleft()
        medicaments.pop()

    elif first + second == 40:
        created_elements["Bandage"] += 1
        textiles.popleft()
        medicaments.pop()

    elif first + second == 100:
        created_elements["MedKit"] += 1
        textiles.popleft()
        medicaments.pop()

    elif first + second > 100:
        created_elements["MedKit"] += 1
        remaining_amount = (first + second) - 100
        textiles.popleft()
        medicaments.pop()
        medicaments[-1] += remaining_amount

    else:
        textiles.popleft()
        medicaments[-1] += 10

sorted_items = dict(sorted(created_elements.items(), key=lambda kvp: (-kvp[1], kvp[0])))

if len(textiles) == 0 and len(medicaments) == 0:
    print("Textiles and medicaments are both empty.")
else:
    if len(textiles) == 0:
        print("Textiles are empty.")
    if len(medicaments) == 0:
        print("Medicaments are empty.")

for key, value in sorted_items.items():
    if value > 0:
        print(f"{key} - {value}")

if len(medicaments) > 0:
    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join(str(el) for el in medicaments)}")
if len(textiles) > 0:
    print(f"Textiles left: {', '.join(str(el) for el in textiles)}")