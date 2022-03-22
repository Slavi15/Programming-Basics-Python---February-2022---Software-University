player_name = str(input())

player_points = 301
successful_shots = 0
unsuccessful_shots = 0

while True:
    space = str(input())

    if space == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())
    
    if space == "Single":
        if points <= player_points:
            player_points -= points
            successful_shots += 1
        else:
            unsuccessful_shots += 1
    elif space == "Double":
        if (points * 2) <= player_points:
            player_points -= (2 * points)
            successful_shots += 1
        else:
            unsuccessful_shots += 1
    elif space == "Triple":
        if (points * 3) <= player_points:
            player_points -= (3 * points)
            successful_shots += 1
        else:
            unsuccessful_shots += 1

    if player_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break