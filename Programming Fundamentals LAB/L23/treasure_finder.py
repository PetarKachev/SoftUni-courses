import re
key = list(map(int, input().split()))
counter = 0
command = input()
messages = []
while command != "find":
    current_message = ''
    for element in command:
        element = ord(element)
        element -= key[counter]
        element = chr(element)
        current_message += element
        counter += 1
        if counter >= len(key):
            counter = 0
    messages.append(current_message)
    counter = 0
    command = input()
first_regex = r'&([A-Za-z]+)&'
second_regex = r'<([A-Za-z\d]+)>'
for current_element in messages:
    first_match = re.findall(first_regex, current_element)
    second_match = re.findall(second_regex, current_element)
    print(f"Found {first_match[0]} at {second_match[0]}")