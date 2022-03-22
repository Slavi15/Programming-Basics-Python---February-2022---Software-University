people_jury = int(input())

all_marks = 0
marks = 0
marks_count = 0

while True:
    topic = str(input())

    if topic == "Finish":
        all_marks_average = all_marks / marks_count
        print(f"Student's final assessment is {all_marks_average:.2f}.")
        break

    for i in range(0, people_jury):
        mark = float(input())
        marks += mark
        marks_count += 1
        all_marks += mark

    average_mark = marks / people_jury
    marks = 0
    print(f"{topic} - {average_mark:.2f}.")