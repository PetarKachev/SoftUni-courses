number = float(input())

if number == 0:
    print('zero')
elif number > 0:
    if number > 0 and number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')
elif number < 0:
    if number > -1 and number < 0:
        print('small negative')
    elif number < - 1000000:
        print('large negative')
    else:
        print('negative')