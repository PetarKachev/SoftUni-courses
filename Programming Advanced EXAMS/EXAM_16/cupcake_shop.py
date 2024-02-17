def stock_availability(box_with_cupcakes, command, *args):

    if command == "delivery":
        box_with_cupcakes = box_with_cupcakes + list(args)

    elif command == "sell":
        if args:
            if str(args[0]).isdigit():
                if args[0] == len(box_with_cupcakes):
                    box_with_cupcakes = []
                else:
                    box_with_cupcakes = box_with_cupcakes[args+1:]
            else:
                box_with_cupcakes = [el for el in box_with_cupcakes if el not in args]
        else:
            box_with_cupcakes = box_with_cupcakes[1:]

    return box_with_cupcakes