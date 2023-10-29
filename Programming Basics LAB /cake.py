cake_length = int(input())
cake_width = int(input())
total_pieces = cake_length * cake_width
no_more_cake = False

data = input()
while data != 'STOP':
    pieces_taken = int(data)
    total_pieces -= pieces_taken

    if total_pieces <= 0:
        no_more_cake = True
        break

    data = input()

diff = abs(total_pieces)
if data == 'STOP':
    print(f"{diff} pieces are left.")
if no_more_cake:
    print(f"No more cake left! You need {diff} pieces more.")
