actor_name = str(input())
academy_points = float(input())
assessor_count = int(input())

all_points = academy_points

for i in range(0, assessor_count):
    assessor_name = str(input())
    assessor_points = float(input())

    points = (len(assessor_name) * assessor_points) / 2
    all_points += points

    if all_points > 1250.5:
        break

diff = abs(all_points - 1250.5)
if all_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")