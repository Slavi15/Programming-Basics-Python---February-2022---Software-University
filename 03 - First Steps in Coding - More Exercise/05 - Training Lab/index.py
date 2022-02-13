w = float(input())
h = float(input())

w_cm = w * 100
h_cm = h * 100

h_without_hall = h_cm - 100
h_places = h_without_hall // 70
w_places = w_cm // 120

places = (h_places * w_places) - 3
print(places)