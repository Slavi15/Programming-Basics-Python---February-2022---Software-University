first_match_result = str(input())
second_match_result = str(input())
third_match_result = str(input())

array = []

first = first_match_result.split(':')
second = second_match_result.split(':')
third = third_match_result.split(':')

array.append(first)
array.append(second)
array.append(third)

won_games = 0
drawn_games = 0
lost_games = 0

for i in array:
    if i[0] > i[1]:
        won_games += 1
    elif i[0] == i[1]:
        drawn_games += 1
    elif i[0] < i[1]:
        lost_games += 1

print(f"""Team won {won_games} games.
Team lost {lost_games} games.
Drawn games: {drawn_games}""")