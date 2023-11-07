input_information = input()

dictionary = {}

while input_information != 'Lumpawaroo':
    if " | " in input_information:
        input_information= input_information.split(" | ")
        force_side = input_information[0]
        force_user = input_information[1]

        user_found = False

        for value in dictionary.values():
            if force_user in value:
                user_found = True
                break

        if not user_found:
            if force_side not in dictionary.keys():
                dictionary[force_side] = []
            dictionary[force_side].append(force_user)

    elif " -> " in input_information:
        input_information = input_information.split(" -> ")
        force_side = input_information[1]
        force_user = input_information[0]

        for value in dictionary.values():
            if force_user in value:
                value.remove(force_user)
                break

        if force_side not in dictionary.keys():
            dictionary[force_side] = []
        dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    input_information = input()

for key, value in dictionary.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')

    for element in value:
        element = f'! {element}'
        print(''.join(element))