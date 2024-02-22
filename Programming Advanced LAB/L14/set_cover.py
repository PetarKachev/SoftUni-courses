def set_cover(universe, sets):

    universe_set = set(universe)
    chosen_sets = []

    while universe_set:
        best_set = max(sets, key=lambda s: len(universe_set.intersection(s)))
        chosen_sets.append(best_set)
        universe_set -= set(best_set)

    return chosen_sets

universe_input = input()
universe = list(map(int, universe_input.split(", ")))

num_sets = int(input())
sets = []

for _ in range(num_sets):
    set_elements = list(map(int, input().split(", ")))
    sets.append(set(set_elements))

result = set_cover(universe, sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print("\nSets to take ({}):".format(len(result)))

for s in result:
    print("{", ",".join(map(str, s)), "}")