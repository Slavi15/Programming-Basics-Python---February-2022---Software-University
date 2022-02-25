junior_cyclists = int(input())
senior_cyclists = int(input())
road_type = str(input())

all_cyclists = junior_cyclists + senior_cyclists
juniors_money = 0
senior_money = 0

if road_type == "trail":
    juniors_money = junior_cyclists * 5.5
    senior_money = senior_cyclists * 7
elif road_type == "cross-country":
    if all_cyclists >= 50:
        juniors_money = junior_cyclists * (8 - (8 * 0.25))
        senior_money = senior_cyclists * (9.5 - (9.5 * 0.25))
    else:
        juniors_money = junior_cyclists * 8
        senior_money = senior_cyclists * 9.5
elif road_type == "downhill":
    juniors_money = junior_cyclists * 12.25
    senior_money = senior_cyclists * 13.75
elif road_type == "road":
    juniors_money = junior_cyclists * 20
    senior_money = senior_cyclists * 21.5

money = juniors_money + senior_money
money -= (money * 0.05)
print(f"{money:.2f}")