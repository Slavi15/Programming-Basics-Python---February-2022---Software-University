start = int(input())
end = int(input())

start_string = str(start)
end_string = str(end)

start_first = int(start_string[0])
start_second = int(start_string[1])
start_third = int(start_string[2])
start_fourth = int(start_string[3])

end_first = int(end_string[0])
end_second = int(end_string[1])
end_third = int(end_string[2])
end_fourth = int(end_string[3])

odd_array = []

for i in range(start_first, end_first + 1):
    for j in range(start_second, end_second + 1):
        for k in range(start_third, end_third + 1):
            for l in range(start_fourth, end_fourth + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    odd_array.append(f"{i}{j}{k}{l}")

print(' '.join(odd_array))