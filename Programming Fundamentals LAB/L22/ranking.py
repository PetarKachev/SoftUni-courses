contests = {}
submissions = {}

contest_command = input()
while contest_command != "end of contests":
    contest_command = contest_command.split(':')
    contest = contest_command[0]
    password_for_contest = contest_command[1]
    contests[contest] = password_for_contest
    contest_command = input()

submission = input()
while submission != "end of submissions":
    submission = submission.split("=>")
    contest = submission[0]
    password = submission[1]
    username = submission[2]
    points = int(submission[3])
    if contest in contests.keys() and password == contests[contest]:
        if username not in submissions.keys():
            submissions[username] = [contest, points]
        else:
            if contest in submissions[username]:
                contest_index = submissions[username].index(contest)
                if submissions[username][contest_index + 1] < points:
                    submissions[username][contest_index + 1] = points
            else:
                submissions[username].append(contest)
                submissions[username].append(points)

    submission = input()

sorted_names = sorted(submissions.keys())

max_value = 0
max_value_name = ''
for name in submissions.keys():
    current_max_value = 0
    for i in range(0, len(submissions[name]), 2):
        current_max_value += submissions[name][i + 1]
    if max_value < current_max_value:
        max_value = current_max_value
        max_value_name = name

print(f"Best candidate is {max_value_name} with total {max_value} points.")
print('Ranking:')

for name in sorted_names:
    nums_list = []
    print(name)
    for i in range(1, len(submissions[name]), 2):
        nums_list.append(submissions[name][i])
        nums_list.sort(reverse=True)
    for number in nums_list:
        index = submissions[name].index(number)
        course = submissions[name][index - 1]
        print(f"#  {course} -> {number}")