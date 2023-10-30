current_student = 0
all_students = 0

name = input()

while name != "Welcome!":
    if len(name) < 5 and name != "Voldemort":
        print(f'{name} goes to Gryffindor.')
        current_student += 1
    elif len(name) == 5 and name != "Voldemort":
        print(f'{name} goes to Slytherin.')
        current_student += 1
    elif len(name) == 6 and name != "Voldemort":
        print(f'{name} goes to Ravenclaw.')
        current_student += 1
    elif len(name) > 6 and name != "Voldemort":
        print(f'{name} goes to Hufflepuff.')
        current_student += 1
    if name == "Voldemort":
        current_student += 1
        break
    all_students += 1
    name = input()

if current_student == all_students:
    print(f'Welcome to Hogwarts.')
if name == "Voldemort":
    print(f'You must not speak of that name!')