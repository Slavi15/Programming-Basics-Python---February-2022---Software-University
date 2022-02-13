import math

series_name = str(input())
episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
relax_duration = break_duration / 4

left_time = break_duration - (lunch_duration + relax_duration)
free_time = math.ceil(abs(left_time - episode_duration))

if left_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {free_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {free_time} more minutes.")