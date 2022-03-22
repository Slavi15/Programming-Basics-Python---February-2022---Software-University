football_team_name = str(input())
played_games = int(input())

total_points = 0
won_games = 0
drawn_games = 0
lost_games = 0

if played_games == 0:
    print(f"{football_team_name} hasn't played any games during this season.")
else:
    for i in range(0, played_games):
        game_result = str(input())

        if game_result == "W":
            won_games += 1
            total_points += 3
        elif game_result == "D":
            drawn_games += 1
            total_points += 1
        elif game_result == "L":
            lost_games += 1

    win_rate = (won_games / played_games) * 100
    print(f"""{football_team_name} has won {total_points} points during this season.
    Total stats:
    ## W: {won_games}
    ## D: {drawn_games}
    ## L: {lost_games}
    Win rate: {win_rate:.2f}%""")