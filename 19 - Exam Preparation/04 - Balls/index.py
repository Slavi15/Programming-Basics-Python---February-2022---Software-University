import math

N = int(input())

total_points = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_divisions_count = 0
others_count = 0

for i in range(0, N):
    ball_type = str(input())

    if ball_type == "red":
        total_points += 5
        red_count += 1
    elif ball_type == "orange":
        total_points += 10
        orange_count += 1
    elif ball_type == "yellow":
        total_points += 15
        yellow_count += 1
    elif ball_type == "white":
        total_points += 20
        white_count += 1
    elif ball_type == "black":
        total_points = math.floor(total_points / 2)
        black_divisions_count += 1
    else:
        others_count += 1

print(f"""Total points: {total_points}
Red balls: {red_count}
Orange balls: {orange_count}
Yellow balls: {yellow_count}
White balls: {white_count}
Other colors picked: {others_count}
Divides from black balls: {black_divisions_count}""")