points = 0
points_array = []

winner_points = 0
winner_name = ""

while True:
    player_name = str(input())

    if player_name == "Stop":
        break
    
    for letter in player_name:
        player_guess = int(input())
        character = chr(player_guess)

        if character == letter:
            points += 10
        else:
            points += 2
    
    points_array.append(points)
    if points >= max(points_array):
        winner_points = points
        winner_name = player_name
    
    points = 0

print(f"The winner is {winner_name} with {winner_points} points!")