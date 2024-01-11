expression = input()
text = []

for char in range(len(expression)):
    if expression[char] == "(":
        text.append(char)
    elif expression[char] == ")":
        start_index = text.pop()
        print(expression[start_index:char + 1])