n = int(input())
my_stack = []

for _ in range(n):
    current_number = input().split(" ")
    if current_number[0] == "1":
        my_stack.append(int(current_number[1]))
    elif my_stack:
        if current_number[0] == "2":
            my_stack.pop()
        elif current_number[0] == "3":
            print(max(my_stack))
        elif current_number[0] == "4":
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end="")
    if my_stack:
        print(', ', end='')