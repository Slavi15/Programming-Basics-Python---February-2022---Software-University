actor_name = str(input())
points = float(input())
assessor_people = int(input())

all_points = 0

for i in range(assessor_people):
    assessor_name = str(input())
    assessor_points = float(input())

    points += ((len(assessor_name) * assessor_points) / 2)

    if points > 1250.5:
        break

diff = abs(points - 1250.5)
if points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")