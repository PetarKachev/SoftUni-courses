number_of_rooms = int(input())
free_chairs = 0
enough_chairs = 0
for i in range(1, number_of_rooms + 1):
    command = input().split(" ")
    chairs = int(len(command[0]))
    people = int(command[1])
    free_chairs += (chairs - people)
    current_free_chairs = people - chairs
    if chairs >= people:
        enough_chairs += 1
        if enough_chairs == number_of_rooms:
            print(f"Game On, {free_chairs} free chairs left")
    else:
        print(f"{current_free_chairs} more chairs needed in room {i}")
