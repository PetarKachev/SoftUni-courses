names = input()
queue = []

while names != "End":
    if names == "Paid":
        for person in queue:
            print(person)
        queue = []
    else:
        queue.append(names)
    names = input()
print(f'{len(queue)} people remaining.')