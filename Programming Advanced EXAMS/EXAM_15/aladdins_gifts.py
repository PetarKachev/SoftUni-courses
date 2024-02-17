from collections import deque
materials = deque(list(map(int, input().split(" "))))
magic_levels = deque(list(map(int, input().split(" "))))

presents = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magic_levels:

    if materials[-1] + magic_levels[0] < 100:

        sum = materials[-1] + magic_levels[0]

        if sum % 2 == 0:

            sum = (materials[-1] * 2) + (magic_levels[0] * 3)

            if 100 <= sum <= 199:
                presents["Gemstone"] += 1
                materials.pop()
                magic_levels.popleft()

            elif 200 <= sum <= 299:
                presents["Porcelain Sculpture"] += 1
                materials.pop()
                magic_levels.popleft()

            elif 300 <= sum <= 399:
                presents["Gold"] += 1
                materials.pop()
                magic_levels.popleft()

            elif 400 <= sum <= 499:
                presents["Diamond Jewellery"] += 1
                materials.pop()
                magic_levels.popleft()

            else:
                materials.pop()
                magic_levels.popleft()

        else:
            sum = (materials[-1] + magic_levels[0]) * 2

            if 100 <= sum <= 199:
                presents["Gemstone"] += 1
                materials.pop()
                magic_levels.popleft()

            elif 200 <= sum <= 299:
                presents["Porcelain Sculpture"] += 1
                materials.pop()
                magic_levels.popleft()

            elif 300 <= sum <= 399:
                presents["Gold"] += 1
                materials.pop()
                magic_levels.popleft()

            elif 400 <= sum <= 499:
                presents["Diamond Jewellery"] += 1
                materials.pop()
                magic_levels.popleft()

            else:
                materials.pop()
                magic_levels.popleft()

    elif 100 <= materials[-1] + magic_levels[0] <= 199:
        presents["Gemstone"] += 1
        materials.pop()
        magic_levels.popleft()

    elif 200 <= materials[-1] + magic_levels[0] <= 299:
        presents["Porcelain Sculpture"] += 1
        materials.pop()
        magic_levels.popleft()

    elif 300 <= materials[-1] + magic_levels[0] <= 399:
        presents["Gold"] += 1
        materials.pop()
        magic_levels.popleft()

    elif 400 <= materials[-1] + magic_levels[0] <= 499:
        presents["Diamond Jewellery"] += 1
        materials.pop()
        magic_levels.popleft()

    elif materials[-1] + magic_levels[0] > 499:

        sum = (materials[-1] + magic_levels[0]) / 2

        if 100 <= sum <= 199:
            presents["Gemstone"] += 1
            materials.pop()
            magic_levels.popleft()

        elif 200 <= sum <= 299:
            presents["Porcelain Sculpture"] += 1
            materials.pop()
            magic_levels.popleft()

        elif 300 <= sum <= 399:
            presents["Gold"] += 1
            materials.pop()
            magic_levels.popleft()

        elif 400 <= sum <= 499:
            presents["Diamond Jewellery"] += 1
            materials.pop()
            magic_levels.popleft()

        else:
            materials.pop()
            magic_levels.popleft()

    else:
        materials.pop()
        magic_levels.popleft()

if presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0 or presents["Gold"] and presents["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if len(materials) > 0:
    print(f"Materials left: {', '.join(str(el) for el in materials)}")
if len(magic_levels) > 0:
    print(f"Magic left: {', '.join(str(el) for el in magic_levels)}")

presents = dict(sorted(presents.items(), key=lambda kvp: kvp[0]))

for key, value in presents.items():
    if value > 0:
        print(f"{key}: {value}")