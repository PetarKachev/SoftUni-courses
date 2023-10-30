sequence_of_strings = input().split(" ")
palindrome = input()
counter = 0
new_list = []
for i in sequence_of_strings:
    if i == palindrome:
        counter += 1
    if i[::-1] == i:
        new_list.append(i)

print(new_list)
print(f'Found palindrome {counter} times')