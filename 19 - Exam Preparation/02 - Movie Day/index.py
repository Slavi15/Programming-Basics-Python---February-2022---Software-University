import math

time_for_shooting = int(input())
number_scenes = int(input())
scene_time = int(input())

time_for_shooting -= (time_for_shooting * 0.15)
time_for_scenes = number_scenes * scene_time

diff = abs(time_for_shooting - time_for_scenes)
if time_for_shooting >= time_for_scenes:
    print(f"You managed to finish the movie on time! You have {math.ceil(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {int(diff)} minutes.")