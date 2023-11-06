name_and_number = input()
dictionary = {}

while len(name_and_number) > 1:
    name_and_number = name_and_number.split("-")
    the_name = name_and_number[0]
    the_number = name_and_number[1]
    dictionary[the_name] = the_number

    name_and_number = input()

number = int(name_and_number)

for i in range(number):
    name = str(input())
    if name in dictionary:
        for key, value in dictionary.items():
            if key == name:
                print(f'{key} -> {value}')
    else:
        print(f"Contact {name} does not exist.")