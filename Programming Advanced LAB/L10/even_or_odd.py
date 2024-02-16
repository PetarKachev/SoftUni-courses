from collections import deque
def even_odd(*args):
    even_nums = []
    odd_nums = []
    args = deque(args)
    func = args.pop()
    for element in args:
        if int(element) % 2 == 0:
            even_nums.append(int(element))
        else:
            odd_nums.append(int(element))
    if func == "odd":
        return odd_nums
    else:
        return even_nums