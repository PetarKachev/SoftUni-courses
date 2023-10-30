sequence_of_integers = list(map(int, input().split(" ")))

if len(sequence_of_integers) == 1:
    print("No")
    exit()

sum_of_all_numbers = 0
counter_of_numbers = 0

for i in range(len(sequence_of_integers)):
  counter_of_numbers += 1
  sum_of_all_numbers += sequence_of_integers[i]

average_number = sum_of_all_numbers / counter_of_numbers

top_five_numbers = []

for j in range(len(sequence_of_integers)):
  if sequence_of_integers[j] > average_number:
    top_five_numbers.append(sequence_of_integers[j])

top_five_numbers.sort(reverse=True)
final_list = []

for i in range(len(top_five_numbers)):
    final_list.append(str(top_five_numbers[i]))
    if len(final_list) == 5:
        break

if len(final_list) == 0:
    print("No")
else:
    print(" ".join(final_list))