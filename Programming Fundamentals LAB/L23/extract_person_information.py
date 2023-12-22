import re
n = int(input())
regex1 = r'@([A-Za-z]+)\|'
regex2 = r'#([\d]+)\*'
for i in range(n):
    info = input()
    first_match = re.findall(regex1, info)
    second_match = re.findall(regex2, info)
    print(f"{first_match[0]} is {second_match[0]} years old.")