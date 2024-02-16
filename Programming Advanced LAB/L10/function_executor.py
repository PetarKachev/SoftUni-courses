def func_executor(*args):
    result = ''
    for func, value in args:
        result += f"{func.__name__} - {func(*value)}\n"
    return result