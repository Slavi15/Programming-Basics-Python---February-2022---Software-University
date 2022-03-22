bad_marks = int(input())

all_marks = 0
earned_bad_marks = 0
tasks_count = 0
tasks_array = []

while True:
    task_name = str(input())
    if task_name == "Enough":
        average_mark = all_marks / tasks_count
        print(f"""Average score: {average_mark:.2f}
        Number of problems: {tasks_count}
        Last problem: {tasks_array[len(tasks_array) - 1]}""")
        break
    else:
        tasks_count += 1
        tasks_array.append(task_name)

    mark = int(input())

    all_marks += mark

    if mark <= 4:
        earned_bad_marks += 1

    if earned_bad_marks == bad_marks:
        print(f"You need a break, {earned_bad_marks} poor grades.")
        break