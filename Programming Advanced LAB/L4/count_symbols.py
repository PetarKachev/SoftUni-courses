string = input()
sorted_string = sorted(string)
my_dict = {}

for element in sorted_string:
    if element not in my_dict:
        my_dict[element] = 1
    else:
        my_dict[element] += 1

for key, value in my_dict.items():
    print(f'{key}: {value} time/s')