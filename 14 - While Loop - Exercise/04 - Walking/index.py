steps_goal = 10000
steps_count = 0

while True:
    value = input()

    if value == "Going home":
        num = int(input())
        steps_count += num
        break
    else:
        steps_count += int(value)

        if steps_count >= steps_goal:
            break

difference = abs(steps_count - steps_goal)

if steps_count >= steps_goal:
    print(f"""Goal reached! Good job!
    {difference} steps over the goal!""")
elif steps_count < steps_goal:
    print(f"{difference} more steps to reach goal.")