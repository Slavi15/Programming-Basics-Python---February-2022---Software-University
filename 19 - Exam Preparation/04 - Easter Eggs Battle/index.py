first_player_eggs = int(input())
second_player_eggs = int(input())

while True:
    value = str(input())

    if value == "End of battle":
        print(f"""Player one has {first_player_eggs} eggs left.
        Player two has {second_player_eggs} eggs left.""")
        break

    if value == "one":
        second_player_eggs -= 1
    elif value == "two":
        first_player_eggs -= 1

    if first_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
        break
    elif second_player_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
        break