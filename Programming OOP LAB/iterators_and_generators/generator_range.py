def genrange(start: int, end: int):
    a = start
    b = end
    while a <= b:
        yield a
        a += 1