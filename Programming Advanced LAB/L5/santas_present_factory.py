from collections import deque
materials = list(map(int, input().split(" ")))
magic = deque(list(map(int, input().split(" "))))

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy test.py", 400: "Bicycle"}
crafted_presents = {}

while materials and magic:
    magic_item = materials[-1] * magic[0]
    if magic_item in presents:
        materials.pop()
        magic.popleft()
        present = presents[magic_item]
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1

    elif magic_item < 0:
        materials.append(materials.pop() + magic.popleft())

    elif magic_item > 0 and magic_item not in presents:
        magic.popleft()
        materials[-1] += 15

    elif materials[-1] <= 0 and magic[0] <= 0:
        magic.popleft()
        materials.pop()
    elif materials[-1] <= 0:
        materials.pop()
    elif magic[0] <= 0:
        magic.popleft()

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or ("Teddy test.py" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(element) for element in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(element) for element in magic])}")

dublicate_dict = sorted(crafted_presents)
for element in dublicate_dict:
    print(f'{element}: {crafted_presents[element]}')