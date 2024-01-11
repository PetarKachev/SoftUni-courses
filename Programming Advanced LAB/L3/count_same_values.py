numbers = list(map(float, input().split(" ")))
dict_nums = {}
for num in numbers:
    if num not in dict_nums:
        dict_nums[num] = 0
for num1 in numbers:
    if num1 in dict_nums.keys():
        dict_nums[num1] += 1
for key, value in dict_nums.items():
    print(f"{key} - {value} times")