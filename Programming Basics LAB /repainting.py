nylon = int(input())
paint_lt = int(input())
razreditel_lt = int(input())
workers_hours = int(input())

price_nylon = (nylon + 2) * 1.50
price_paint = (paint_lt * 1.1) * 14.50
price_razreditel = razreditel_lt * 5.00
#bag_price = 0.40

total_sum_materials = price_nylon + price_paint + price_razreditel + 0.40
total_sum_workers = (total_sum_materials * 0.3) * workers_hours
total_amount = total_sum_materials + total_sum_workers

print(total_amount)
