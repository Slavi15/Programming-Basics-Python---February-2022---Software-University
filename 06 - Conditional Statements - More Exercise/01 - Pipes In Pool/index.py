volume = int(input())
first_flow_per_hour = int(input())
second_flow_per_hour = int(input())
absent_hours = float(input())

first_litres = first_flow_per_hour * absent_hours
second_litres = second_flow_per_hour * absent_hours
total_litres = first_litres + second_litres

if total_litres <= volume:
    percentage_fill = (total_litres / volume) * 100
    first_fill_percentage = (first_litres / total_litres) * 100
    second_fill_percentage = (second_litres / total_litres) * 100
    print(f"The pool is {percentage_fill:.2f}% full. Pipe 1: {first_fill_percentage:.2f}%. Pipe 2: {second_fill_percentage:.2f}%.")
elif total_litres > volume:
    overflow = abs(total_litres - volume)
    print(f"For {absent_hours} hours the pool overflows with {overflow:.2f} liters.")
