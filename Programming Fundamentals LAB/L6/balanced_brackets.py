lines = int(input())

balanced = True
there_is_open_bracket = False

for _ in range(0, lines):
    character = input()

    if character != "(" and character != ")":
        continue

    open_bracket = character == "("
    if there_is_open_bracket == open_bracket:
        balanced = False
        break

    there_is_open_bracket = open_bracket

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")