from collections import deque
from logic import verification

matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
first_player = input("Prémier joueur nom: ")
second_player = input("Deuxième joueur nom: ")

players = deque([first_player, second_player])

player_symbols = {}

first_player_symbol = input(f"{first_player} vous voulez jouer avec 'X' ou 'O'?")

while True:

    if first_player_symbol == "X":
        player_symbols[first_player] = "X"
        player_symbols[second_player] = "O"
        break

    elif first_player_symbol == "O":
        player_symbols[first_player] = "O"
        player_symbols[second_player] = "X"
        break

    else:
        print("Essayez avec 'X' ou 'O'.")
        first_player_symbol = input(f"{first_player} voulez-vous jouer avec 'X' ou 'O'?")
        continue

print("C'est la numeration du tableau:")
print('| 1 | 2 | 3 |')
print('| 4 | 5 | 6 |')
print('| 7 | 8 | 9 |')
print(f'{first_player} commence prémier!')

while True:
    current_position = input(f"{players[0]} choisissez une position s'il vous plait [1-9]:")

    if current_position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print(f"Essayez avec un nombre entre 1 et 9")
        continue

    print(verification(matrix, current_position, players[0], player_symbols))

    players.rotate(-1)