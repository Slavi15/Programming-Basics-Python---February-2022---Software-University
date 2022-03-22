country = str(input())
appliance = str(input())

difficulty_points = 0
performance_points = 0

if country == "Russia":
    if appliance == "ribbon":
        difficulty_points += 9.1
        performance_points += 9.4
    elif appliance == "hoop":
        difficulty_points += 9.3
        performance_points += 9.8
    elif appliance == "rope":
        difficulty_points += 9.6
        performance_points += 9
elif country == "Bulgaria":
    if appliance == "ribbon":
        difficulty_points += 9.6
        performance_points += 9.4
    elif appliance == "hoop":
        difficulty_points += 9.55
        performance_points += 9.75
    elif appliance == "rope":
        difficulty_points += 9.5
        performance_points += 9.4
elif country == "Italy":
    if appliance == "ribbon":
        difficulty_points += 9.2
        performance_points += 9.5
    elif appliance == "hoop":
        difficulty_points += 9.45
        performance_points += 9.35
    elif appliance == "rope":
        difficulty_points += 9.7
        performance_points += 9.15

all_points = difficulty_points + performance_points
diff = 20 - all_points
percent = (diff / 20) * 100

print(f"""The team of {country} get {all_points:.3f} on {appliance}.
{percent:.2f}%""")