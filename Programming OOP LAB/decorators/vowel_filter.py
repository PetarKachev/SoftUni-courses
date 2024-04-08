def vowel_filter(function):

    def wrapper():
        result = function()     # We call that function
        return [el for el in result if el in 'aeyoui']

    return wrapper  # Refer the function, don't call it