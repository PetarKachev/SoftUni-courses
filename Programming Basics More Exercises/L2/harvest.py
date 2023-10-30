from math import floor, ceil

vineyard_area = int(input())
grape_per_sq_m = float(input())
wine_required_lt = int(input())
workers = int(input())

grape = vineyard_area * grape_per_sq_m
harvest_for_wine = 0.40 * grape
wine = harvest_for_wine / 2.5

diff = abs(wine_required_lt - wine)
wine_per_worker = diff / workers

if wine < wine_required_lt:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_per_worker)} liters per person.")    