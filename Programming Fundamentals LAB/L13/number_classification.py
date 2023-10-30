numbers = list(map(int, input().split(", ")))
positive = [str(positive) for positive in numbers if positive >= 0]
negative = [str(negative) for negative in numbers if negative < 0]
even = [str(even) for even in numbers if even % 2 == 0]
odd = [str(odd) for odd in numbers if odd % 2 != 0]
print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')