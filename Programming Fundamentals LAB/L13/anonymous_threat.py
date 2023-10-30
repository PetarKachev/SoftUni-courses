def int_to_chr(word):
    string = list(word)
    new_list = list()

    while string[0].isdigit():
        new_list.append(string[0])
        string.pop(0)

    num = int("".join(new_list))
    string.insert(0, chr(num))
    return ''.join(string)

def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)

print(" ".join([switch_letters(int_to_chr(word)) for word in input().split()]))