first_parameter = input()
second_parameter = int(input())
third_parameter = int(input())

def action(first, second, third):
    if first == "multiply":
        return second * third
    elif first == "divide":
        return int(second / third)
    elif first == "add":
        return second + third
    elif first == "subtract":
        return second - third

print(action(first_parameter, second_parameter, third_parameter))