string = list(input())
number_of_explosions = 0
for char in range(len(string)):
    if string[char] == ">":
        number_of_explosions += int(string[char + 1])
    else:
        if number_of_explosions > 0:
            string[char] = '*'
            number_of_explosions -= 1
string = [char for char in string if char != '*']
print(''.join(string))