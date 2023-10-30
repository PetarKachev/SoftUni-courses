key = int(input())

n = int(input())
final_string = ""
for i in range(n):
    letter = input()
    transformed_number = ord(letter) + key
    transformed_number = str(chr(transformed_number))
    final_string += transformed_number

print(final_string)
