players_pool = {}

line = input()
while line != "Season end":

    if " -> " in line:
        line = line.split(' -> ')
        player, position, skill = str(line[0]), str(line[1]), int(line[2])

        if player not in players_pool.keys():
            players_pool[player] = {position: skill}
        elif position not in players_pool[player]:
            players_pool[player][position] = skill
        elif players_pool[player][position] < skill:
            players_pool[player][position] = skill

    elif " vs " in line:
        line = line.split(' vs ')
        player1, player2 = str(line[0]), str(line[1])

        if player1 not in players_pool.keys() or player2 not in players_pool.keys():
            line = input()
            continue

        for curr_position in players_pool[player1].keys():
            if curr_position in players_pool[player2].keys():
                a = sum(x for x in players_pool[player1].values())
                b = sum(x for x in players_pool[player2].values())
                if a > b:
                    del players_pool[player2]
                    break
                elif a < b:
                    del players_pool[player1]
                    break
                else:
                    break

    line = input()

sorted_players = dict(sorted(players_pool.items(), key=lambda x: sum(x[1].values()), reverse=True))
# We sort by the sum of skill points of every player
for key, value in sorted_players.items():
    skill_points = sum(x for x in sorted_players[key].values())
    print(f"{key}: {skill_points} skill")
    sorted_items = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    # We sort by skill points and by name
    for k2, v2 in sorted_items.items():
        print(f"- {k2} <::> {v2}")