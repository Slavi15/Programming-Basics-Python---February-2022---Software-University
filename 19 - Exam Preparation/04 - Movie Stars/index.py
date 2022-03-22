actors_budget = float(input())

while True:
    actor_name = str(input())

    if actor_name == "ACTION":
        break

    if len(actor_name) > 15:
        actors_budget -= (actors_budget * 0.2)
    else:
        salary = float(input())
        actors_budget -= salary

    if actors_budget < 0:
        break

if actors_budget >= 0:
    print(f"We are left with {actors_budget:.2f} leva.")
else:
    print(f"We need {abs(actors_budget):.2f} leva for our actors.")