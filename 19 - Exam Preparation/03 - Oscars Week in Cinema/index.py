movie_name = str(input())
room_type = str(input())
tickets_count = int(input())

money = 0

if room_type == "normal":
    if movie_name == "A Star Is Born":
        money = tickets_count * 7.5
    elif movie_name == "Bohemian Rhapsody":
        money = tickets_count * 7.35
    elif movie_name == "Green Book":
        money = tickets_count * 8.15
    elif movie_name == "The Favourite":
        money = tickets_count * 8.75
elif room_type == "luxury":
    if movie_name == "A Star Is Born":
        money = tickets_count * 10.5
    elif movie_name == "Bohemian Rhapsody":
        money = tickets_count * 9.45
    elif movie_name == "Green Book":
        money = tickets_count * 10.25
    elif movie_name == "The Favourite":
        money = tickets_count * 11.55
elif room_type == "ultra luxury":
    if movie_name == "A Star Is Born":
        money = tickets_count * 13.5
    elif movie_name == "Bohemian Rhapsody":
        money = tickets_count * 12.75
    elif movie_name == "Green Book":
        money = tickets_count * 13.25
    elif movie_name == "The Favourite":
        money = tickets_count * 13.95

print(f"{movie_name} -> {money:.2f} lv.")