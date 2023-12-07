import re
text = input()
regex = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.finditer(regex, text)
all_pairs = 0
valid_pairs = []
for match in matches:
    all_pairs += 1
    if match.group(2) == match.group(3)[::-1]:
        valid_pairs.append(f'{match.group(2)} <=> {match.group(3)}')
if all_pairs == 0 and len(valid_pairs) == 0:
    print("No word pairs found!")
    print("No mirror words!")
elif all_pairs > 0 and len(valid_pairs) == 0:
    print(f"{all_pairs} word pairs found!")
    print("No mirror words!")
else:
    print(f"{all_pairs} word pairs found!")
    print('The mirror words are:')
    print(', '.join(valid_pairs))