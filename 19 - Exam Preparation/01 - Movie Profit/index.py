movie_name = str(input())
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percent = int(input())

money = days_count * tickets_count * ticket_price
money -= (money * (cinema_percent / 100))

print(f"The profit from the movie {movie_name} is {money:.2f} lv.")