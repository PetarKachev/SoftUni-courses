encrypted_message = input()
new_string = ''
for char in encrypted_message:
    new_string += chr(ord(char) + 3)
print(new_string)