n = int(input())
word = input()

first_list = []
second_list = []

for i in range(n):
    string = input()
    first_list.append(string)
    if word in string:
        second_list.append(string)

print(first_list)
print(second_list)
