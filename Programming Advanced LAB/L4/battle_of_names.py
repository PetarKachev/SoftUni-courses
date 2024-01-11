n = int(input())
even_set = set()
odd_set = set()

for i in range(1, n + 1):
    name = input()
    current_ascii_sum = 0
    for character in name:
        current_ascii_sum += ord(character)
    current_final_sum = int(current_ascii_sum / i)

    if current_final_sum % 2 == 0:
        even_set.add(current_final_sum)
    else:
        odd_set.add(current_final_sum)

if sum(odd_set) == sum(even_set):
    for element in even_set:
        odd_set.add(element)
    odd_set = [str(element) for element in odd_set]
    print(", ".join(odd_set))

elif sum(odd_set) < sum(even_set):
    for element in even_set:
        odd_set.add(element)
    odd_set = [str(element) for element in odd_set]
    print(", ".join(odd_set))

elif sum(odd_set) > sum(even_set):
    odd_set = [str(element) for element in odd_set]
    print(", ".join(odd_set))