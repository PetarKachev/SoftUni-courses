def naughty_or_nice_list(*args, **kwargs):
    from collections import deque
    list_with_kids = {"Nice": [], "Naughty": [], "Not found": []}
    args = deque(args)
    santas_list = args.popleft()
    numbers = []
    names = []
    for element in santas_list:
        numbers.append(element[0])
        names.append(element[1])

    for command in args:
        command = command.split("-")

        if command[1] == "Naughty":
            if numbers.count(int(command[0])) == 1:
                needed_index = numbers.index(int(command[0]))
                list_with_kids["Naughty"].append(names[needed_index])
                numbers.pop(needed_index)
                names.pop(needed_index)

        elif command[1] == "Nice":
            if numbers.count(int(command[0])) == 1:
                needed_index = numbers.index(int(command[0]))
                list_with_kids["Nice"].append(names[needed_index])
                numbers.pop(needed_index)
                names.pop(needed_index)

    if kwargs:
        for key, value in kwargs.items():

            if value == "Nice":
                if names.count(key) == 1:
                    list_with_kids["Nice"].append(key)
                    needed_index = names.index(key)
                    numbers.pop(needed_index)
                    names.pop(needed_index)

            elif value == "Naughty":
                if names.count(key) == 1:
                    list_with_kids["Naughty"].append(key)
                    needed_index = names.index(key)
                    numbers.pop(needed_index)
                    names.pop(needed_index)

    if len(names) > 0:
        for name in names:
            list_with_kids["Not found"].append(name)
    result = ''

    if len(list_with_kids["Nice"]) > 0:
        nice_names = ', '.join(list_with_kids["Nice"])
        result += f'Nice: {nice_names}\n'

    if len(list_with_kids["Naughty"]) > 0:
        naughty_names = ', '.join(list_with_kids["Naughty"])
        result += f"Naughty: {naughty_names}\n"

    if len(list_with_kids["Not found"]) > 0:
        not_found_names = ', '.join(list_with_kids["Not found"])
        result += f"Not found: {not_found_names}\n"

    return result