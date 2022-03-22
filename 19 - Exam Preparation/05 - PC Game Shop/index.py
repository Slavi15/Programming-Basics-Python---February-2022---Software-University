sold_games_count = int(input())

hearthstone_games = 0
fortnite_games = 0
overwatch_games = 0
others = 0

for i in range(0, sold_games_count):
    game_name = str(input())

    if game_name == "Hearthstone":
        hearthstone_games += 1
    elif game_name == "Fornite":
        fortnite_games += 1
    elif game_name == "Overwatch":
        overwatch_games += 1
    else:
        others += 1

p1 = (hearthstone_games / sold_games_count) * 100
p2 = (fortnite_games / sold_games_count) * 100
p3 = (overwatch_games / sold_games_count) * 100
p4 = (others / sold_games_count) * 100

print(f"""Hearthstone - {p1:.2f}%
Fornite - {p2:.2f}%
Overwatch - {p3:.2f}%
Others - {p4:.2f}%""")