neightbourhood_size = list(map(int, input().split("@")))

command = input()
current_position = 0

while command != "Love!":
    command = command.split(" ")
    lenght_of_jump = int(command[1])

    if current_position + lenght_of_jump >= len(neightbourhood_size):
        current_position = 0
    else:
        current_position += lenght_of_jump

    if neightbourhood_size[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")

    if neightbourhood_size[current_position] > 0:
        neightbourhood_size[current_position] -= 2
        if neightbourhood_size[current_position] == 0:
            print(f"Place {current_position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_position}.")

if sum(neightbourhood_size) == 0:
    print(f"Mission was successful.")
else:
    houses_without_valenine = [number for number in neightbourhood_size if number > 0]
    print(f"Cupid has failed {len(houses_without_valenine)} places.")