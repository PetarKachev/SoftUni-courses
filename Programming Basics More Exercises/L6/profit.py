one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_bills = int(input())
amount = int(input())

for i in range(0, one_lev_coins + 1):
    for j in range(0, two_lev_coins + 1):
        for k in range(0, five_lev_bills + 1):
            if (i * 1) + (j * 2) + (k * 5) == amount:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {amount} lv.")
