input_info = list(map(int, input().split()))

def numbers(numbers):
    negative_sum = []
    positive_sum = []
    for element in numbers:
        if element < 0:
            negative_sum.append(element)
        else:
            positive_sum.append(element)

    negative_result = sum(negative_sum)
    positive_result = sum(positive_sum)
    if abs(negative_result) > abs(positive_result):
        print(negative_result)
        print(positive_result)
        print("The negatives are stronger than the positives")
    else:
        print(negative_result)
        print(positive_result)
        print("The positives are stronger than the negatives")

numbers(input_info)