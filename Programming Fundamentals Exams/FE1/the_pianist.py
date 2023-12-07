n = int(input())

dictionary = {}

for i in range(n):
    current_info = input()
    current_info = current_info.split("|")

    piece = current_info[0]
    composer = current_info[1]
    key = current_info[2]

    dictionary[piece] = []
    dictionary[piece].append(composer)
    dictionary[piece].append(key)

command = input()

while command != "Stop":
    command = command.split("|")

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece not in dictionary.keys():
            dictionary[piece] = []
            dictionary[piece].append(composer)
            dictionary[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":
        piece = command[1]

        if piece in dictionary.keys():
            del dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]

        if piece in dictionary.keys():
            dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for key, value in dictionary.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")