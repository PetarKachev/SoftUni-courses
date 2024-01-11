n, m = list(map(int, input().split(" ")))
first_set = set()
second_set = set()
common_set = set()

for i in range(1, n + m + 1):
    num = int(input())
    if i <= n:
        first_set.add(num)
    else:
        second_set.add(num)

for element in first_set:
    if element in second_set:
        common_set.add(element)

for current_element in common_set:
    print(current_element)