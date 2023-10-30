all_people = input().split(" ")
skipped_people = int(input())
executed_people = []
counter = 0
index = 0

while len(all_people) > 0:
    counter += 1

    if counter % skipped_people == 0:
        executed_people.append(all_people.pop(index))
    else:
        index += 1

    if index >= len(all_people):
        index = 0

print(str(executed_people).replace(' ', '').replace('\'', ""))