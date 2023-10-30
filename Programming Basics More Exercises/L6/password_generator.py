n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, l + 97):
            for m in range(97, l + 97):
                for o in range(1, n + 1):
                    if o <= i or o <= j:
                        continue
                    print(f"{i}{j}{chr(k)}{chr(m)}{o}", end=" ")