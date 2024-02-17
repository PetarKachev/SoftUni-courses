def numbers_searching(*args):
    args = sorted(args)
    dublicate_list = []
    missing_number = 0

    for num in args:
        if args.count(num) > 1:
            if num not in dublicate_list:
                dublicate_list.append(num)
                dublicate_list = sorted(dublicate_list)

    for number in range(args[0], args[-1] + 1):
        if number not in args:
            missing_number = number

    return [missing_number, dublicate_list]