first_player_name = str(input())
second_player_name = str(input())

first_player_points = 0
second_player_points = 0

while True:
    first_player_card = input()

    if first_player_card == "End of game":
        print(f"""{first_player_name} has {first_player_points} points
        {second_player_name} has {second_player_points} points""")
        break

    second_player_card = int(input())

    if int(first_player_card) > second_player_card:
        points = int(first_player_card) - second_player_card
        first_player_points += points
    elif int(first_player_card) < second_player_card:
        points = second_player_card - int(first_player_card)
        second_player_points += points
    elif int(first_player_card) == second_player_card:
        print('Number wars!')
        new_first_card = int(input())
        new_second_card = int(input())
        if new_first_card > new_second_card:
            print(f"{first_player_name} is winner with {first_player_points} points")
            break
        elif new_first_card < new_second_card:
            print(f"{second_player_name} is winner with {second_player_points} points")
            break