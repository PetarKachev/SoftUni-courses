n = int(input())
positive_list = []
negative_list = []
even_list = []
odd_list = []
for i in range(n):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    if number < 0:
        negative_list.append(number)
    if number % 2 == 0:
        even_list.append(number)
    if number % 2 != 0:
        odd_list.append(number)
command = input()
if command == "positive":
    print(positive_list)
elif command == "negative":
    print(negative_list)
elif command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
