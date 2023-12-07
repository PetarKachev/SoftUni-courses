import re

text = input()

regex = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

matches = re.findall(regex, text)

print(' '.join(matches))