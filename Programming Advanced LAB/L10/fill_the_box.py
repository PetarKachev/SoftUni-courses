def fill_the_box(*args):
    args = list(args)
    result = 1
    for num in args[:3]:
        result *= num
    box_space = result
    args = args[3:]
    score = 0

    for element in args:
        if str(element).isdigit():
            score += element
        else:
            if box_space > score:
                return f"There is free space in the box. You could put {box_space - score} more cubes."
                break
            else:
                return f"No more free space! You have {score - box_space} more cubes."
                break
