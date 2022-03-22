best_player_name = ""
best_player_goals = 0

while True:
    player_name = str(input())

    if player_name == "END":
        break
    
    scored_goals = int(input())

    if scored_goals > best_player_goals:
        best_player_goals = scored_goals
        best_player_name = player_name

    if scored_goals >= 10:
        break

print(f"{best_player_name} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")