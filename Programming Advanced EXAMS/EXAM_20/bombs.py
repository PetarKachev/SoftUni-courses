from collections import deque
bomb_effects = deque(list(map(int, input().split(", "))))
bomb_casings = deque(list(map(int, input().split(", "))))

made_bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_effects and bomb_casings:

    first_element = bomb_effects[0]
    second_element = bomb_casings[-1]

    if first_element + second_element == 40:
        made_bombs["Datura Bombs"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif first_element + second_element == 60:
        made_bombs["Cherry Bombs"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif first_element + second_element == 120:
        made_bombs["Smoke Decoy Bombs"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    else:
        bomb_casings[-1] -= 5

    if made_bombs["Datura Bombs"] >= 3 and made_bombs["Cherry Bombs"] >= 3 and made_bombs["Smoke Decoy Bombs"] >= 3:
        break

if made_bombs["Datura Bombs"] >= 3 and made_bombs["Cherry Bombs"] >= 3 and made_bombs["Smoke Decoy Bombs"] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) == 0:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects)}")

if len(bomb_casings) == 0:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings)}")

print(f'Cherry Bombs: {made_bombs["Cherry Bombs"]}')
print(f'Datura Bombs: {made_bombs["Datura Bombs"]}')
print(f'Smoke Decoy Bombs: {made_bombs["Smoke Decoy Bombs"]}')