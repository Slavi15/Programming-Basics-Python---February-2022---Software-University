competition_days = int(input())

money = 0
money_for_day = 0

won_games = 0
lost_games = 0

win = 0
loss = 0

for i in range(0, competition_days):
    while True:
        sport = str(input())
        if sport == "Finish":
            money += money_for_day
            if won_games > lost_games:
                win += 1
                money += (money_for_day * 0.1)
                won_games = 0
                lost_games = 0
                money_for_day = 0
            else:
                loss += 1
                won_games = 0
                lost_games = 0
                money_for_day = 0
            break

        result = str(input())

        if result == "win":
            money_for_day += 20
            won_games += 1
        elif result == "lose":
            lost_games += 1

if win > loss:
    money += (money * 0.2)
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")