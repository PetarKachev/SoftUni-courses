rows = int(input())
sum = 0

for i in range(rows):
    data = list(map(int, input().split(" ")))

    for element in data:
        sum += data[i]
        break

print(sum)