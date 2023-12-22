submissions = {}
users = {}

while True:
    line = input()
    if line == "no more time":
        break
    line = line.split(" -> ")
    username = str(line[0])
    contest = str(line[1])
    points = int(line[2])

    if contest not in submissions:
        submissions[contest] = {username:points}
    elif username not in submissions[contest]:
        submissions[contest][username] = points
    elif submissions[contest][username] < points:
        submissions[contest][username] = points

    if username not in users:
        users[username] = {contest:points}
    elif contest not in users[username]:
        users[username][contest] = points
    elif users[username][contest] < points:
        users[username][contest] = points

for key, value in submissions.items():
    i = 1
    print(f'{key}: {len(value)} participants')
    sorted_items = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    for key2, value2 in sorted_items.items():
        print(f'{i}. {key2} <::> {value2}')
        i += 1
print('Individual standings:')
sorted_names = dict(sorted(users.items(), key=lambda x: (-sum(x[1].values()), x[0])))
i = 1
for k, v in sorted_names.items():
    print(f'{i}. {k} -> {sum(v.values())}')
    i += 1