text = input()

list_with_emoticons = []

for char in range(len(text)):
    current_emoji = ''
    if text[char] == ":":
        current_emoji += text[char]
        current_emoji += text[char + 1]
        list_with_emoticons.append(current_emoji)

for emoji in list_with_emoticons:
    print(emoji)