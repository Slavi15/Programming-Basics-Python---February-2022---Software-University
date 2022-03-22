pc_count = int(input())

sells = 0
all_rating = 0

for i in range(0, pc_count):
    number = str(input())

    rating = int(number[2:len(number)])
    possible_sells = int(number[0:2])

    all_rating += rating

    if rating == 2:
        sells += 0
    elif rating == 3:
        sells += (possible_sells * 0.5)
    elif rating == 4:
        sells += (possible_sells * 0.7)
    elif rating == 5:
        sells += (possible_sells * 0.85)
    elif rating == 6:
        sells += possible_sells

average_rating = all_rating / pc_count
print(f"""{sells:.2f}
{average_rating:.2f}""")