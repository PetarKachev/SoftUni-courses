def flights(*args):
    from collections import deque
    args = deque(args)
    dict_with_info = {}

    while args[0] != "Finish":

        if args[0] not in dict_with_info.keys():
            dict_with_info[args[0]] = args[1]
            args.popleft()
            args.popleft()
        else:
            dict_with_info[args[0]] += args[1]
            args.popleft()
            args.popleft()

    return dict_with_info