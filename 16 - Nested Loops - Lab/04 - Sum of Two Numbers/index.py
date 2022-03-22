start = int(input())
end = int(input())
magic_number = int(input())

combinations_number = 0
result_encounter = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        result = i + j
        combinations_number += 1

        if result == magic_number:
            result_encounter += 1
            if result_encounter == 1:
                print(f"Combination N:{combinations_number} ({i} + {j} = {magic_number})")
        elif i == end and j == end and result_encounter == 0:
            print(f"{combinations_number} combinations - neither equals {magic_number}")