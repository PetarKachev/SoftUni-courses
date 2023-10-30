initial_energy = int(input())

battles_won = 0

command = input()

while command != "End of battle":
    command = int(command)

    if initial_energy - command >= 0:
        battles_won += 1
        initial_energy -= command
        if battles_won % 3 == 0:
            initial_energy += battles_won

    else:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy')
        break

    command = input()

else:
    print(f'Won battles: {battles_won}. Energy left: {initial_energy}')
