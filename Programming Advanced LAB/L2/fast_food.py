from collections import deque
food_quantity = int(input())
int_sequence = list(map(int, input().split()))
print(max(int_sequence))

int_sequence = deque(int_sequence)

while len(int_sequence) > 0:
    if food_quantity >= int_sequence[0]:
        food_quantity -= int_sequence[0]
        int_sequence.popleft()
    else:
        break
int_sequence = [str(char) for char in int_sequence]

if len(int_sequence) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(int_sequence)}")