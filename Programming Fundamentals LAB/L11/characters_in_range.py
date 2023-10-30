first_char = input()
second_char = input()

def ASCII(first, second):
    for i in range(ord(first_char) + 1, ord(second_char), 1):
        print(chr(i), end=" ")

ASCII(first_char, second_char)