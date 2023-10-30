integers = list(map(int, input().split()))
command = input()
shot_targets = 0
while command != "End":
    index = command
    if int(index) + 1 <= len(integers):
        chosen_number = integers[int(index)]
        for i in range(len(integers)):
            if integers[i] > chosen_number:
                integers[i] = integers[i] - chosen_number
            elif chosen_number >= integers[i] and int(integers[i]) != - 1:
                    integers[i] = integers[i] + chosen_number
        integers[int(index)] = - 1
        shot_targets += 1
    command = input()
string_integers = []
for i in integers:
    string_integers.append(str(i))
result = " ".join(string_integers)
print(f'Shot targets: {shot_targets} -> {result}')