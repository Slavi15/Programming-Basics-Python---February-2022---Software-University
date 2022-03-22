minutes = int(input())
seconds = int(input())
length_metres = float(input())
seconds_100_metres = int(input())

control_in_seconds = (minutes * 60) + seconds
time_decrease = length_metres / 120
all_time_decrease = time_decrease * 2.5

time = ((length_metres / 100) * seconds_100_metres) - all_time_decrease

if time <= control_in_seconds:
    print(f"""Marin Bangiev won an Olympic quota!
    His time is {time:.3f}.""")
else:
    diff = abs(time - control_in_seconds)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")