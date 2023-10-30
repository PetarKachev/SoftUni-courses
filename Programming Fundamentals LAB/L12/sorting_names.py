string_with_names = input().split(", ")

result = sorted(string_with_names, key=lambda x: (-len(x), x))

print(result)
