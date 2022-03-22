import math

competitions_count = int(input())
starting_points = int(input())

won_points = 0
won_competitions = 0

for i in range(0, competitions_count):
    competition_phase = str(input())

    if competition_phase == "W":
        starting_points += 2000
        won_points += 2000
        won_competitions += 1
    elif competition_phase == "F":
        starting_points += 1200
        won_points += 1200
    elif competition_phase == "SF":
        starting_points += 720
        won_points += 720

average_points = won_points / competitions_count
percent = (won_competitions / competitions_count) * 100

print(f"""Final points: {starting_points}
Average points: {math.floor(average_points)}
{percent:.2f}%""")