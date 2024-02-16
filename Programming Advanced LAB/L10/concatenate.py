def concatenate(*args, ** kwargs):
    word = ''
    for element in args:
        word += element
    for key, value in kwargs.items():
        if key in word:
            word = word.replace(key, value)
    return word