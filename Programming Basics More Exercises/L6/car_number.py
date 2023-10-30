beginning = int(input())
ending = int(input())

for i in range(beginning, ending + 1):
    for j in range(beginning, ending + 1):
        for k in range(beginning, ending + 1):
            for l in range(beginning, ending + 1):

                if i % 2 == 0 and l % 2 == 1:
                    if i > l and (j + k) % 2 == 0:
                        print(f"{i}{j}{k}{l}", end=" ")

                elif i % 2 == 1 and l % 2 == 0:
                    if i > l and (j + k) % 2 == 0:
                        print(f"{i}{j}{k}{l}", end=" ")
