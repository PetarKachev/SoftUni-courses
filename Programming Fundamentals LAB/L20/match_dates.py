import re

text = input()

regex = r"\d{2}/[A-Z]{1}[a-z]{2}/\d{4}|\d{2}\.[A-Z]{1}[a-z]{2}\.\d{4}|\d{2}-[A-Z]{1}[a-z]{2}-\d{4}"
matches = re.findall(regex, text)

for match in matches:
    if "/" in match:
        match = match.split("/")
        day = match[0]
        month = match[1]
        year = match[2]
        print(f'Day: {day}, Month: {month}, Year: {year}')

    elif "." in match:
        match = match.split(".")
        day = match[0]
        month = match[1]
        year = match[2]
        print(f'Day: {day}, Month: {month}, Year: {year}')

    elif "-" in match:
        match = match.split("-")
        day = match[0]
        month = match[1]
        year = match[2]
        print(f'Day: {day}, Month: {month}, Year: {year}')