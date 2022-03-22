movie_name = ""
points = 0
most_points = 0
array = []

for i in range(0, 7):
    value = str(input())

    if value == "STOP":
        break
    elif i == 6:
        print("The limit is reached.")

    for letter in value:
        ascii_code = ord(letter)
        points += ord(letter)

        if ascii_code >= 97 and ascii_code <= 122:
            points -= (2 * len(value))
        elif ascii_code >= 65 and ascii_code <= 90:
            points -= len(value)

    if i == 0:
        array.append(points)
        most_points = points
        movie_name = value
    elif i > 0:
        if points > max(array):
            array.append(points)
            most_points = points
            movie_name = value

    points = 0

print(f"The best movie for you is {movie_name} with {most_points} ASCII sum.")