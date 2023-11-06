list_of_char = input().split(", ")

dictionary = {}

for i in range(len(list_of_char)):
    key = list_of_char[i]
    value = ord(key)
    dictionary[key] = value

print(dictionary)