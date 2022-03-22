name = str(input())

all_marks = 0
marks_count = 0
exclusion_count = 0

while True:
    mark = float(input())
    all_marks += mark
    marks_count += 1

    if mark < 4:
        exclusion_count += 1

    if exclusion_count > 1:
        print(f"{name} has been excluded at {marks_count - 1} grade")
        break

    if marks_count == 12:
        average_mark = all_marks / marks_count
        print(f"{name} graduated. Average grade: {average_mark:.2f}")
        break