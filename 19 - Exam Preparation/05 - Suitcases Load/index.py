trunk_capacity = float(input())

suitcase_count = 0

while True:
    suitcase_volume = input()

    if suitcase_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    if trunk_capacity < float(suitcase_volume):
        print("No more space!")
        break
    
    suitcase_count += 1
    if suitcase_count % 3 == 0:
        volume = float(suitcase_volume) + (float(suitcase_volume) * 0.1)
        trunk_capacity -= volume
    else:
        trunk_capacity -= float(suitcase_volume)

print(f"Statistic: {suitcase_count} suitcases loaded.")