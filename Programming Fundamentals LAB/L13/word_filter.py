words = input().split(" ")

new_list = [word for word in words if len(word) % 2 == 0]

for i in new_list:
    print(str(i))