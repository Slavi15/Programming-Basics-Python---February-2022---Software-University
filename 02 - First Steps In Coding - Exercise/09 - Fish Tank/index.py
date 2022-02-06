cm_length = int(input())
cm_width = int(input())
cm_height = int(input())
percent = float(input())

volume = cm_length * cm_width * cm_height
litres = volume / 1000
needed_litres = litres - (litres * (percent / 100))

print(needed_litres)