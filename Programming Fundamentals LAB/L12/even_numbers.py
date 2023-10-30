numbers = list(map(int, input().split(", ")))

found_or_not_found = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))

even_indices = list(filter(lambda a: a != 'no', found_or_not_found))

print(even_indices)