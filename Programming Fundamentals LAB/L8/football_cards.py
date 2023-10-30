string = input().split(" ")

team_A = [f'A-{s}' for s in range(1, 11 + 1, 1)]
team_B = [f'B-{j}' for j in range(1, 11 + 1, 1)]
game_was_terminated = False
for element in string:
    if element in team_A:
        team_A.remove(element)
    elif element in team_B:
        team_B.remove(element)
    if len(team_A) < 7 or len(team_B) < 7:
        game_was_terminated = True
        break

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
if game_was_terminated:
    print('Game was terminated')
