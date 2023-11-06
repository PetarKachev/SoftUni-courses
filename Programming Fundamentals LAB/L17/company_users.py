company_info = input()

dictionary = {}

while company_info != "End":
    company_info = company_info.split(" -> ")

    name = company_info[0]
    start_id = company_info[1]
    id = f'-- {start_id}'

    if name not in dictionary.keys():
        dictionary[name] = id
    else:
        if id not in dictionary[name]:
            dictionary[name] += f'/{id}'
    company_info = input()

for key, value in dictionary.items():
    current_value = value.split("/")
    print(f'{key}')
    print("\n".join(current_value))