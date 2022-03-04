number_of_groups = int(input())

all_people = 0
musala_people = 0
monblan_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0

for i in range(number_of_groups):
    people_in_group = int(input())
    all_people += people_in_group

    if people_in_group <= 5:
        musala_people += people_in_group
    elif people_in_group >= 6 and people_in_group <= 12:
        monblan_people += people_in_group
    elif people_in_group >= 13 and people_in_group <= 25:
        kilimanjaro_people += people_in_group
    elif people_in_group >= 26 and people_in_group <= 40:
        k2_people += people_in_group
    elif people_in_group >= 41:
        everest_people += people_in_group

p1 = (musala_people / all_people) * 100
p2 = (monblan_people / all_people) * 100
p3 = (kilimanjaro_people / all_people) * 100
p4 = (k2_people / all_people) * 100
p5 = (everest_people / all_people) * 100

print(f"""{p1:.2f}%
{p2:.2f}%
{p3:.2f}%
{p4:.2f}%
{p5:.2f}%""")