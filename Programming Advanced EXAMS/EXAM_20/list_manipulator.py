def list_manipulator(current_list, first_command, second_command, *args):

    if first_command == "add" and second_command == "beginning":

        args = list(args)
        current_list = args + current_list
        return current_list

    elif first_command == "add" and second_command == "end":

        args = list(args)
        current_list = current_list + args
        return current_list

    elif first_command == "remove" and second_command == "beginning":

        if args:
            current_list = current_list[args[0]:]
        else:
            current_list = current_list[1:]
        return current_list

    elif first_command == "remove" and second_command == "end":

        if args:
            current_list = current_list[::-1]
            current_list = current_list[args[0]:]
            current_list = current_list[::-1]
        else:
            current_list = current_list[:-1]

        return current_list