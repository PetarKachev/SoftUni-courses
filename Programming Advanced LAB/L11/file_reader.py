import os
path_file = "text.txt"

try:
    if os.path.exists(path_file):
        the_file = open("text.txt", "r")
        sum = 0
        for current_file in the_file:
            sum += int(current_file)
        print(sum)
except FileNotFoundError:
    print("Le fichier n'est pas trouvé, l'opération est impossible")