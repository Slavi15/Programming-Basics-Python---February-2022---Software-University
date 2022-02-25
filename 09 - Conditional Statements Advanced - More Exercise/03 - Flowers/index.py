chrysantemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = str(input())
holiday = str(input())

chrysantemum_price = 0
roses_price = 0
tulips_price = 0
price = 0

flowers_count = chrysantemum_count + roses_count + tulips_count

if season == "Spring":
    if holiday == "Y":
        chrysantemum_price = chrysantemum_count * (2 + (2 * 0.15))
        roses_price = roses_count * (4.1 + (4.1 * 0.15))
        tulips_price = tulips_count * (2.5 + (2.5 * 0.15))
        price = chrysantemum_price + roses_price + tulips_price
    elif holiday == "N":
        chrysantemum_price = chrysantemum_count * 2
        roses_price = roses_count * 4.1
        tulips_price = tulips_count * 2.5
        price = chrysantemum_price + roses_price + tulips_price

    if tulips_count > 7:
            price -= (price * 0.05)

    if flowers_count > 20:
        price -= (price * 0.2)
elif season == "Summer":
    if holiday == "Y":
        chrysantemum_price = chrysantemum_count * (2 + (2 * 0.15))
        roses_price = roses_count * (4.1 + (4.1 * 0.15))
        tulips_price = tulips_count * (2.5 + (2.5 * 0.15))
        price = chrysantemum_price + roses_price + tulips_price
    elif holiday == "N":
        chrysantemum_price = chrysantemum_count * 2
        roses_price = roses_count * 4.1
        tulips_price = tulips_count * 2.5
        price = chrysantemum_price + roses_price + tulips_price

    if flowers_count > 20:
        price -= (price * 0.2)
elif season == "Autumn":
    if holiday == "Y":
        chrysantemum_price = chrysantemum_count * (3.75 + (3.75 * 0.15))
        roses_price = roses_count * (4.5 + (4.5 * 0.15))
        tulips_price = tulips_count * (4.15 + (4.15 * 0.15))
        price = chrysantemum_price + roses_price + tulips_price
    elif holiday == "N":
        chrysantemum_price = chrysantemum_count * 3.75
        roses_price = roses_count * 4.5
        tulips_price = tulips_count * 4.15
        price = chrysantemum_price + roses_price + tulips_price

    if flowers_count > 20:
        price -= (price * 0.2)
elif season == "Winter":
    if holiday == "Y":
        chrysantemum_price = chrysantemum_count * (3.75 + (3.75 * 0.15))
        roses_price = roses_count * (4.5 + (4.5 * 0.15))
        tulips_price = tulips_count * (4.15 + (4.15 * 0.15))
        price = chrysantemum_price + roses_price + tulips_price
    elif holiday == "N":
        chrysantemum_price = chrysantemum_count * 3.75
        roses_price = roses_count * 4.5
        tulips_price = tulips_count * 4.15
        price = chrysantemum_price + roses_price + tulips_price

    if roses_count >= 10:
            price -= (price * 0.1)

    if flowers_count > 20:
        price -= (price * 0.2)

price += 2
print(f"{price:.2f}")