import re
text = input()
regex = r'(::|\*\*)([A-Z]{1}[a-z]{2,})\1'

treshold = 1
for character in text:
    if character.isdigit():
        treshold *= int(character)
matches = re.findall(regex, text)
all_emojis = 0
cool_emojis =  []
for match in matches:
    all_emojis += 1
    word = match[1]
    emoji = match[0] + match[1] + match[0]
    current_coolness = 0
    for character in word:
        current_coolness += ord(character)
    if current_coolness > treshold:
        cool_emojis.append(emoji)
print(f"Cool threshold: {treshold}")
print(f"{all_emojis} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)