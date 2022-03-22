kozunak_count = int(input())
peels_with_eggs_count = int(input())
cookies_kg = int(input())

kozunak_price = 3.2
eggs_price = 4.35
cookies_price = 5.4
eggs_dye_per_egg_price = 0.15

kozunak = kozunak_count * kozunak_price
eggs = peels_with_eggs_count * eggs_price
cookies = cookies_kg * cookies_price
dye_price = peels_with_eggs_count * 12 * eggs_dye_per_egg_price

expenses = kozunak + eggs + cookies + dye_price
print(f"{expenses:.2f}")