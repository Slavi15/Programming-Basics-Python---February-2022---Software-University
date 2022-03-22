desired_value = int(input())

starting_height = desired_value - 30
unsuccessful_jumps_count = 0
all_jumps_count = 0

while True:
    height = int(input())

    all_jumps_count += 1
    if height > starting_height:
        if unsuccessful_jumps_count > 0:
            unsuccessful_jumps_count = 0
        starting_height += 5
    elif height <= starting_height:
        unsuccessful_jumps_count += 1
        if unsuccessful_jumps_count == 3:
            print(f"Tihomir failed at {starting_height}cm after {all_jumps_count} jumps.")
            break

    if starting_height > desired_value:
        print(f"Tihomir succeeded, he jumped over {desired_value}cm after {all_jumps_count} jumps.")
        break