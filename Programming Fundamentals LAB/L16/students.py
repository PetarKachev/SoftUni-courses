command = input()
list_with_all_info = []

while True:
    command = command.split(":")
    if len(command) == 1:
        break
    name = str(command[0])
    points = int(command[1])
    course = str(command[2])
    list_with_all_info.append(name)
    list_with_all_info.append(points)
    list_with_all_info.append(course)
    command = input()

the_exam = "".join(command)
counter = 0
for element in list_with_all_info:
    counter += 1
    if counter % 3 == 0:
        if element[0:5] == the_exam[0:5]:
            key = list_with_all_info[counter - 3]
            value = list_with_all_info[counter - 2]
            print(f'{key} - {value}')
