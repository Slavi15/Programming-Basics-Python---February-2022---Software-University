chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.4
vegetarian_menu_price = 8.15

chicken_price = chicken_menu_price * chicken_menu_count
fish_price = fish_menu_price * fish_menu_count
vegetarian_price = vegetarian_menu_price * vegetarian_menu_count

price_without_delivery = chicken_price + fish_price + vegetarian_price
dessert_price = price_without_delivery * 0.2

price = price_without_delivery + dessert_price + 2.5

print(format(price, '.2f'))