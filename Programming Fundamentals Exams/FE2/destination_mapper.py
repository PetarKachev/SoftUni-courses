import re

text = input()

regex = r'([=\/])([A-Z]{1}[A-Za-z]{2,})\1'
matches = re.finditer(regex, text)
destinations = []
total_points = 0

for match in matches:
    destinations.append(match.group(2))
    total_points += len(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")