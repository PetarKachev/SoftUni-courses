number = int(input())

def perfect_number(num):
    sum_of_dividors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_dividors += i

    if sum_of_dividors == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

perfect_number(number)