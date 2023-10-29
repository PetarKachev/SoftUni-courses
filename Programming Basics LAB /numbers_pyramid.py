n = int(input())
current_num = 1
flag = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(current_num, end=' ')

        if current_num == n:
            flag = True
            break

        current_num += 1

    print()
    if flag:
        break
