lenght = int(input())
width = int(input())
height = int(input())
percent_dec = float(input())

volume = lenght * width * height
total_lt = volume / 1000
dec_volume = total_lt * (percent_dec / 100)

result = total_lt - dec_volume

print(result)