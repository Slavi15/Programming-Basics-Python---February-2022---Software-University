first_sector = 'A'
last_sector = str(input())
sector_rows = int(input())

places_odd_row = int(input())
places_even_row = places_odd_row + 2

first_sector_number = ord(first_sector) - 96
last_sector_number = ord(last_sector) - 96

array = []

for i in range(first_sector_number, last_sector_number + 1):
    for row in range(1, sector_rows + 1):
        if row % 2 != 0:
            for k in range(1, places_odd_row + 1):
                place = chr(k + 96)
                sector = chr(i + 96)
                array.append(f"{sector}{row}{place}")
        elif row % 2 == 0:
            for k in range(1, places_even_row + 1):
                place = chr(k + 96)
                sector = chr(i + 96)
                array.append(f"{sector}{row}{place}")
    sector_rows += 1

print('\n'.join(array))
print(len(array))