n = int(input())

my_list = []

for name in range(n):
    current_name = input()
    if " " in current_name:
        current_name = current_name.split(" ")
    else:
        for element in my_list:
            if element in current_name:
                break
        else:
            if current_name not in my_list:
                my_list.append(current_name)

for element in my_list:
    if len(element) > 0:
        print(element)