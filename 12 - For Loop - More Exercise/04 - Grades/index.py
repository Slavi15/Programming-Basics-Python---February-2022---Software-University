students_count = int(input())

all_marks = 0

between_2_and_3 = 0
between_3_and_4 = 0
between_4_and_5 = 0
bigger_5 = 0

for i in range(students_count):
    mark = float(input())
    all_marks += mark

    if mark >= 2 and mark < 3:
        between_2_and_3 += 1
    elif mark >= 3 and mark < 4:
        between_3_and_4 += 1
    elif mark >= 4 and mark < 5:
        between_4_and_5 += 1
    elif mark >= 5:
        bigger_5 += 1

p1 = (between_2_and_3 / students_count) * 100
p2 = (between_3_and_4 / students_count) * 100
p3 = (between_4_and_5 / students_count) * 100
p4 = (bigger_5 / students_count) * 100
average_mark = all_marks / students_count

print(f"""Top students: {p4:.2f}%
Between 4.00 and 4.99: {p3:.2f}%
Between 3.00 and 3.99: {p2:.2f}%
Fail: {p1:.2f}%
Average: {average_mark:.2f}""")