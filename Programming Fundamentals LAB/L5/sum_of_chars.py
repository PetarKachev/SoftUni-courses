n = int(input())

sum_of_chars = 0

for i in range(n):
    current_string = input()
    sum_of_chars += ord(current_string)

print(f'The sum equals: {sum_of_chars}')