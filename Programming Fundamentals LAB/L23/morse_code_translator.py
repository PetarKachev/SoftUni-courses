input_info = list(map(str, input().split(" | ")))

message = ''

for element in input_info:
    if " " in element:
        element = element.split(" ")
        for current_element in element:
            if current_element == ".-":
                message += "A"
            elif current_element == "-...":
                message += "B"
            elif current_element == "-.-.":
                message += "C"
            elif current_element == "-..":
                message += "D"
            elif current_element == ".":
                message += "E"
            elif current_element == "..-.":
                message += "F"
            elif current_element == "--.":
                message += "G"
            elif current_element == "....":
                message += "H"
            elif current_element == "..":
                message += "I"
            elif current_element == ".---":
                message += "J"
            elif current_element == "-.-":
                message += "K"
            elif current_element == ".-..":
                message += "L"
            elif current_element == "--":
                message += "M"
            elif current_element == "-.":
                message += "N"
            elif current_element == "---":
                message += "O"
            elif current_element == ".--.":
                message += "P"
            elif current_element == "--.-":
                message += "Q"
            elif current_element == ".-.":
                message += "R"
            elif current_element == "...":
                message += "S"
            elif current_element == "-":
                message += "T"
            elif current_element == "..-":
                message += "U"
            elif current_element == "...-":
                message += "V"
            elif current_element == ".--":
                message += "W"
            elif current_element == "-..-":
                message += "X"
            elif current_element == "-.--":
                message += "Y"
            elif current_element == "--..":
                message += "Z"
    else:
        if element == ".-":
            message += "A"
        elif element == "-...":
            message += "B"
        elif element == "-.-.":
            message += "C"
        elif element == "-..":
            message += "D"
        elif element == ".":
            message += "E"
        elif element == "..-.":
            message += "F"
        elif element == "--.":
            message += "G"
        elif element == "....":
            message += "H"
        elif element == "..":
            message += "I"
        elif element == ".---":
            message += "J"
        elif element == "-.-":
            message += "K"
        elif element == ".-..":
            message += "L"
        elif element == "--":
            message += "M"
        elif element == "-.":
            message += "N"
        elif element == "---":
            message += "O"
        elif element == ".--.":
            message += "P"
        elif element == "--.-":
            message += "Q"
        elif element == ".-.":
            message += "R"
        elif element == "...":
            message += "S"
        elif element == "-":
            message += "T"
        elif element == "..-":
            message += "U"
        elif element == "...-":
            message += "V"
        elif element == ".--":
            message += "W"
        elif element == "-..-":
            message += "X"
        elif element == "-.--":
            message += "Y"
        elif element == "--..":
            message += "Z"
    message += ' '
print(message)