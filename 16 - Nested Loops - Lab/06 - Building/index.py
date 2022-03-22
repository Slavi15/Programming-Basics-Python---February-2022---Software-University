floors_count = int(input())
rooms_per_floor = int(input())

iteration_count = 0
final_array = []
array = []

if floors_count == 1:
    for i in range(floors_count, 0, -1):
        for j in range(0, rooms_per_floor):
            array.append(f"L{i}{j}")
            if j == rooms_per_floor - 1:
                print(' '.join(array))
                break
else:
    for i in range(floors_count, -1, -1):
        iteration_count += 1
        if iteration_count > 1:
            final_array.append(array)
            array = []

        for j in range(0, rooms_per_floor):
            if floors_count % 2 == 0:
                if i == floors_count:
                    array.append(f"L{i}{j}")
                elif iteration_count % 2 == 0:
                    array.append(f"A{i}{j}")
                elif iteration_count % 2 != 0 and i != floors_count:
                    array.append(f"O{i}{j}")
            elif floors_count % 2 != 0:
                if i == floors_count:
                    array.append(f"L{i}{j}")
                elif iteration_count % 2 == 0:
                    array.append(f"O{i}{j}")
                elif iteration_count % 2 != 0 and i != floors_count:
                    array.append(f"A{i}{j}")

if len(final_array) > 0:
    for i in final_array:
        print(' '.join(i))