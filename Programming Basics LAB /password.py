username = input()
user_password = input()

while True:
    current_password = input()
    if current_password == user_password:
        print(f"Welcome {username}!")
        break
