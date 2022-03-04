import math

competitions_count = int(input())
points = int(input())

won_competitions = 0
competitions_points = 0

for i in range(competitions_count):
    text = str(input())

    if text == 'W':
        points += 2000
        competitions_points += 2000
        won_competitions += 1
    elif text == 'F':
        points += 1200
        competitions_points += 1200
    elif text == 'SF':
        points += 720
        competitions_points += 720

average_points = competitions_points / competitions_count
win_percentage = (won_competitions / competitions_count) * 100

print(f"Final points: {points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{win_percentage:.2f}%")