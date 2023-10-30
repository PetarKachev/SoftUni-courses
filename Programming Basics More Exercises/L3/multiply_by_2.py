input_number = float(input())
while input_number >= 0:
    number = input_number * 2
    print(f"Result: {number:.2f}")

    input_number = float(input())
else:
    print("Negative number!")
