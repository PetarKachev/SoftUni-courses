total_pages = int(input())
pages_for_hour = int(input())
days = int(input())

hours_to_read = total_pages // pages_for_hour
hours_per_day = hours_to_read // days

print(hours_per_day)