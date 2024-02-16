def math_operations(*args, **kwargs):
    counter = 0
    for num in range(len(args)):
        counter += 1
        if counter == 1:
            kwargs['a'] += args[num]
        elif counter == 2:
            kwargs['s'] -= args[num]
        elif counter == 3:
            if args[counter - 1]:
                kwargs['d'] /= args[num]
        elif counter == 4:
            kwargs['m'] *= args[num]
            counter = 0
    sorted_dict = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    result = ""
    for key, value in sorted_dict.items():
        result += f'{key}: {value:.1f}\n'
    return result