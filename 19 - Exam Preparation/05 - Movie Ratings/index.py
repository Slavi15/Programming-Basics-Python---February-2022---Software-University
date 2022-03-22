movies_count = int(input())

max_rating_movie = ""
min_rating_movie = ""
rating_array = []
all_ratings = 0

for i in range(0, movies_count):
    movie_name = str(input())
    movie_rating = float(input())

    all_ratings += movie_rating

    if i == 0:
        rating_array.append(movie_rating)
        max_rating_movie = movie_name
    elif i > 0:
        if movie_rating > max(rating_array):
            max_rating_movie = movie_name
        elif movie_rating < min(rating_array):
            min_rating_movie = movie_name
        
        rating_array.append(movie_rating)

average_rating = all_ratings / movies_count

print(f"""{max_rating_movie} is with highest rating: {max(rating_array):.1f}
{min_rating_movie} is with lowest rating: {min(rating_array):.1f}
Average rating: {average_rating:.1f}""")