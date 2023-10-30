integer_string = list(map(int, input().split(", ")))
group = 0
while len(integer_string) > 0:
    group += 10
    list = [number for number in integer_string if number <= group]
    for i in list:
        if i in integer_string:
            integer_string.remove(i)
    print(f"Group of {group}'s: {list}")
    list = []
