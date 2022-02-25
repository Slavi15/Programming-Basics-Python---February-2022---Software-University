projection_type = str(input())
rows_count = int(input())
columns_count = int(input())

price = 0

if projection_type == "Premiere":
    price = rows_count * columns_count * 12
elif projection_type == "Normal":
    price = rows_count * columns_count * 7.5
elif projection_type == "Discount":
    price = rows_count * columns_count * 5

print(f"{price:.2f} leva")