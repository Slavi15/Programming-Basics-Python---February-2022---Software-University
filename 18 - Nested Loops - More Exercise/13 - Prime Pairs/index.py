import math

start_number_first_pair = int(input())
start_number_second_pair = int(input())
diff_first_pair = int(input())
diff_second_pair = int(input())

end_number_first_pair = start_number_first_pair + diff_first_pair
end_number_second_pair = start_number_second_pair + diff_second_pair

array = []

for i in range(start_number_first_pair, end_number_first_pair + 1):
    for j in range(start_number_second_pair, end_number_second_pair + 1):
        first_num = 0
        second_num = 0

        first_prime_flag = 0
        second_prime_flag = 0

        for x in range(2, int(math.sqrt(i)) + 1):
            if i % x == 0:
                first_prime_flag = 1
                break
        if first_prime_flag == 0:
            first_num = i
                
        for y in range(2, int(math.sqrt(j)) + 1):
            if j % y == 0:
                second_prime_flag = 1
                break
        if second_prime_flag == 0:
            second_num = j

        if first_num != 0 and second_num != 0:
            array.append(f"{i}{j}")

print('\n'.join(array))