countries = input().split(", ")
capitals = input().split(", ")

zipped_element = list(tuple(zip(countries, capitals)))

for element in zipped_element:
    print(" -> ".join(element))