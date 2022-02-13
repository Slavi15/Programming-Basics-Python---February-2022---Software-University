record_seconds = float(input())
distance_meters = float(input())
seconds_one_meter = float(input())

swimming_seconds = distance_meters * seconds_one_meter
added_time = (distance_meters // 15) * 12.5
total_time = swimming_seconds + added_time

needed_time = abs(total_time - record_seconds)

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif total_time >= record_seconds:
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")