movie_name = str(input())
movie_packet = str(input())
tickets_count = int(input())

money = 0

if movie_name == "John Wick":
    if movie_packet == "Drink":
        money = tickets_count * 12
    elif movie_packet == "Popcorn":
        money = tickets_count * 15
    elif movie_packet == "Menu":
        money = tickets_count * 19
elif movie_name == "Star Wars":
    if movie_packet == "Drink":
        money = tickets_count * 18
    elif movie_packet == "Popcorn":
        money = tickets_count * 25
    elif movie_packet == "Menu":
        money = tickets_count * 30

    if tickets_count >= 4:
        money -= (money * 0.3)
elif movie_name == "Jumanji":
    if movie_packet == "Drink":
        money = tickets_count * 9
    elif movie_packet == "Popcorn":
        money = tickets_count * 11
    elif movie_packet == "Menu":
        money = tickets_count * 14

    if tickets_count == 2:
        money -= (money * 0.15)

print(f"Your bill is {money:.2f} leva.")