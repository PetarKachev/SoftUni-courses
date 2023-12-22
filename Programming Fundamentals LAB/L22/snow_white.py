dwarfs = {}
result_list = []

name_d = "name"
hat_d = "hat"
physic_d = "physic"
hat_len = "hat len"

line = input()
while line != "Once upon a time":
    line = line.split(" <:> ")
    name, color, physics = str(line[0]), str(line[1]), int(line[2])

    if color not in dwarfs.keys():
        dwarfs[color] = {name: physics}
    elif name not in dwarfs[color].keys():
        dwarfs[color][name] = physics
    elif dwarfs[color][name] < physics:
        dwarfs[color][name] = physics

    line = input()

for hat in dwarfs.keys():
    for name, physic in dwarfs[hat].items():
        result_list.append({hat_len: len(dwarfs[hat]), name_d: name, physic_d: physic, hat_d: hat})

sorted_result = sorted(result_list, key=lambda item: (-item[physic_d], -item[hat_len]))

for show in sorted_result:
    print(f"({show[hat_d]}) {show[name_d]} <-> {show[physic_d]}")