import math

record_in_seconds = float(input())
length_in_metres = float(input())
seconds_per_metre = float(input())

seconds = length_in_metres * seconds_per_metre
additional_seconds = math.floor(length_in_metres / 50) * 30
all_seconds = seconds + additional_seconds

diff = abs(all_seconds - record_in_seconds)
if all_seconds >= record_in_seconds:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f" Yes! The new record is {all_seconds:.2f} seconds.")