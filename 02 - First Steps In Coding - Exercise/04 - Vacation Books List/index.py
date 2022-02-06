import math

pages_in_book = int(input())
pages_per_hour = int(input())
days_for_book = int(input())

needed_time_for_book = pages_in_book / pages_per_hour
hours_per_day = needed_time_for_book / days_for_book

print(math.floor(hours_per_day))