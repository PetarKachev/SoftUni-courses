gift_list = input().split(" ")
command = input()

while command != "No Money":
    command = command.split(" ")
    if "OutOfStock" in command:
        for i in range(len(gift_list)):
            if command[1] == gift_list[i]:
                gift_list[i] = "None"
    elif "Required" in command:
        for i in range(len(gift_list)):
            if i == int(command[2]):
                gift_list[i] = command[1]
    elif "JustInCase" in command:
        for i in range(len(gift_list)):
            gift_list[-1] = command[1]
    command = input()
while "None" in gift_list:
    gift_list.remove("None")
for i in gift_list:
    print(i, end=" ")