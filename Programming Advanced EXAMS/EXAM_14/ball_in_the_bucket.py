rows = 6
cols = 6
matrix = []
for row in range(rows):
    data = input().split(" ")
    matrix.append(data)
collected_points = 0
throw_balls = 3
commands = []

first_throw = input()
second_throw = input()
third_throw = input()
commands.append(first_throw)
commands.append(second_throw)
commands.append(third_throw)

for command in commands:
    command = command.split(", ")
    row = int(command[0][1:])
    col = int(command[1][:-1])

    if 0 <= row < rows and 0 <= col < cols:

        if matrix[row][col] == "B":
            matrix[row][col] = "x"

            for i in range(len(matrix)):
                if matrix[i][col] != "x":
                    collected_points += int(matrix[i][col])
            throw_balls -= 1
            if throw_balls == 0:
                break

if 100 <= collected_points <= 199:
    print(f"Good job! You scored {collected_points} points, and you've won Football.")

elif 200 <= collected_points <= 299:
    print(f"Good job! You scored {collected_points} points, and you've won Teddy Bear.")

elif collected_points >= 300:
    print(f"Good job! You scored {collected_points} points, and you've won Lego Construction Set.")

else:
    print(f"Sorry! You need {100 - collected_points} points more to win a prize.")