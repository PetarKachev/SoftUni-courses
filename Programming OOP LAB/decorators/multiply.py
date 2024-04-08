def multiply(num):

    def decorator(function):

        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * num

        return wrapper
    return decorator