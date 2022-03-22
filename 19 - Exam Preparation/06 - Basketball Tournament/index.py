won_games = 0
lost_games = 0
all_matches_count = 0

while True:
    competition_name = str(input())

    if competition_name == "End of tournaments":
        p1 = (won_games / all_matches_count) * 100
        p2 = (lost_games / all_matches_count) * 100
        print(f"""{p1:.2f}% matches win
        {p2:.2f}% matches lost""")
        break

    match_count = int(input())
    all_matches_count += match_count

    for i in range(1, match_count + 1):
        desi_team_points = int(input())
        other_team_points = int(input())

        if desi_team_points > other_team_points:
            won_games += 1
            print(f"Game {i} of tournament {competition_name}: win with {abs(desi_team_points - other_team_points)} points.")
        elif desi_team_points < other_team_points:
            lost_games += 1
            print(f"Game {i} of tournament {competition_name}: lost with {abs(desi_team_points - other_team_points)} points.")