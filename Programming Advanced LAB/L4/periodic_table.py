n = int(input())
unique_elements = set()

for i in range(n):
    elements = input().split(" ")
    for current_element in elements:
        if current_element not in unique_elements:
            unique_elements.add(current_element)

for element in unique_elements:
    print(element)