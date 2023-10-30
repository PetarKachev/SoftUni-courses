password = input()

def pass_verification(word):
    number_of_validation = 0
    count_of_the_digits = 0
    if 6 <= len(word) <= 10:
        number_of_validation += 1
    else:
        print("Password must be between 6 and 10 characters")
    if word.isalnum():
        number_of_validation += 1
    else:
        print("Password must consist only of letters and digits")
    for num in word:
        if num.isnumeric():
            count_of_the_digits += 1
    if count_of_the_digits >= 2:
        number_of_validation += 1
    else:
        print("Password must have at least 2 digits")
    if number_of_validation == 3:
        print("Password is valid")

pass_verification(password)

