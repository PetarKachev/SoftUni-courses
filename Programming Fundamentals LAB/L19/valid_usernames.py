usernames = list(map(str, input().split(", ")))
valid_user_names = []
for username in usernames:
    valid_chars = 0
    if 3 <= len(username) <= 16:
        for letter in username:
            if letter.isalpha() or letter.isdigit() or letter == "-" or letter == "_":
                valid_chars += 1
        if valid_chars == len(username):
            valid_user_names.append(username)
        else:
            continue
for name in valid_user_names:
    print(name)