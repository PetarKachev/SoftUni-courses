standard_tickets = 0
students_tickets = 0
kids_tickets = 0
total_tickets = 0

input_line = input()
while input_line != 'Finish':
    movie = input_line
    capacity = int(input())

    current_tickets = 0
    command_line = input()
    while command_line != 'End':
        ticket_type = command_line
        current_tickets += 1
        total_tickets += 1
        if command_line == 'standard':
            standard_tickets += 1
        elif command_line == 'student':
            students_tickets += 1
        elif command_line == 'kid':
            kids_tickets += 1

        if current_tickets == capacity: break
        command_line = input()

    current_percent = (current_tickets / capacity) * 100
    print(f"{movie} - {current_percent:.2f}% full.")
    input_line = input()

percent_students = (students_tickets / total_tickets) * 100
percent_standard = (standard_tickets / total_tickets) * 100
percent_kids = (kids_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
