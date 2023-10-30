string = input().split(", ")


def polindrome(number):
    for number in string:
        if number[::-1] == number:
            print(f'True')
        else:
            print(f'False')


polindrome(string)