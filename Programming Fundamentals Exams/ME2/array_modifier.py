array_integers = list(map(int, input().split()))

command = input()

while command != "end":
    command = command.split()
    new_list = []
    if command[0] == "swap":
        first_index_swap = int(command[1])
        second_index_swap = int(command[2])
        array_integers[first_index_swap], array_integers[second_index_swap] = array_integers[second_index_swap], array_integers[first_index_swap]
    elif command[0] == "multiply":
        first_index_multiply = int(command[1])
        second_index_multiply = int(command[2])
        array_integers[first_index_multiply] = array_integers[first_index_multiply] * array_integers[second_index_multiply]
    elif command[0] == "decrease":
        for i in range(len(array_integers)):
            array_integers[i] -= 1
    command = input()

result =""
for i in range(0, len(array_integers) - 1):
    result += str(array_integers[i]) + ", "

print(result + str(array_integers[-1]))