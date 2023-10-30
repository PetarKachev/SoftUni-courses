from string import ascii_letters

c_crash = False
o_crash = False
n_crash = False
word = ""

input_line = input()
while input_line != "End":
    if input_line in ascii_letters:
        if input_line == 'c' and not c_crash:  # False
            c_crash = True
        elif input_line == 'o' and not o_crash:  # False
            o_crash = True
        elif input_line == 'n' and not n_crash:  # False
            n_crash = True
        else:
            word += input_line

    if c_crash and o_crash and n_crash:  # True
        c_crash = False
        o_crash = False
        n_crash = False
        print(word, end=" ")
        word = ""

    input_line = input()
