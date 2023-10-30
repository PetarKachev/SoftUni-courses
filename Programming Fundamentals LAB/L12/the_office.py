list_of_employees = list(map(int, input().split(" ")))
happiness_factor = int(input())

happy_employees = list(map(lambda x: x * happiness_factor, list_of_employees))

average_happiness = 0
sum = 0
number = 0
for i in happy_employees:
    sum += int(i)
    number += 1
average = sum / number
new_list = [number for number in happy_employees if number > average]

if len(new_list) >= len(happy_employees) / 2:
    print(f"Score: {len(new_list)}/{len(happy_employees)}. Employees are happy!")
else:
    print(f"Score: {len(new_list)}/{len(happy_employees)}. Employees are not happy!")