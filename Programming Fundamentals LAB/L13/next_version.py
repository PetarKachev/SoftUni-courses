current_version = list(map(str, input().split(".")))
current_string = "".join(current_version)
current_string = int(current_string)

while True:
    current_string += 1
    if current_string:
        print(".".join(str(current_string)))
        break
    if current_string == 400:
        break